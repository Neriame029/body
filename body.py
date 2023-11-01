import cv2
import mediapipe as mp
import socket
import threading

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
# For webcam input:
cap = cv2.VideoCapture(0)

exit = False
results_handList = [0] * 2
tmp= [0] * 2


def adjust(handList):
    results_handList[0] = handList[0]+tmp[0]
    results_handList[1] = handList[1]+tmp[1]
    print("sucsess")
    tmp[0]=results_handList[0]
    tmp[1]=results_handList[1]
    return results_handList

def detect():
    global results_hand
    results_hand = [0] * 2
    global hand
    hand = [0] * 2  #left_hand

    with mp_pose.Pose(
        min_detection_confidence=0.5,min_tracking_confidence=0.5) as pose:

        while cap.isOpened():
            fps = cap.get(cv2.CAP_PROP_FPS)
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            
            success, image = cap.read()
            
            if not success:
                print("Ignoring empty camera frame.")
                continue

            # 後でセルフィービューで表示するために、画像を水平に反転させる。
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = pose.process(image)

            # 画像上にポーズの目印を描く。
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)       

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                xhand=results.pose_landmarks.landmark[15].x
                yhand=results.pose_landmarks.landmark[15].y

                hand[0]= int(xhand*100-results_hand[0])
                hand[1]= int((yhand*-1)*100-results_hand[1])

                cv2.circle(image, (int(xhand*width),int(yhand*height)), 5, (255, 255, 255), thickness=-1, lineType=cv2.LINE_8, shift=0)
            else :
                hand[0]=1000
                hand[1]=1000

            
            ##print(hand[0],hand[1])    

            # UDPで送信
            host = "localhost"
            port = 5000

            # データを指定のフォーマットに整形(コンマ区切り)
            data = f"{hand[0]},{hand[1]}"

            # UDPソケットを作成
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.sendto(data.encode("utf-8"), (host, port))

            cv2.imshow('MediaPipe Pose', image)

            key = cv2.waitKey(5)
            # if key & 0xFF == ord('r') :
            #         results_hand=adjust(hand)

            if key & 0xFF == 27:##Esc
                exit = True
                break

        cap.release()

def listen():
    global results_hand
    host = "localhost"
    port = 5001

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))
        word=f"UDP server is listening on {host}:{port}"

        try:
            while True:
                data, _ = server_socket.recvfrom(1024)
                data = data.decode("utf-8")
                print(data)
                if data == "reset":
                    results_hand = adjust(hand)
                if exit:
                    break
                
        except KeyboardInterrupt:
            print("Server terminated by user.")

t1 = threading.Thread(target=detect)
t2 = threading.Thread(target=listen)
t1.start()
t2.start()
t1.join()
t2.join()