import socket
import cv2

word = "reset"
script = "finish"
cv2.namedWindow("WindowName", cv2.WINDOW_NORMAL)  # ウィンドウを作成

while True:
    key = cv2.waitKey(5)
    if key & 0xFF == ord('r'):
        print("r")
        # UDPで送信
        host = "localhost"
        port = 5001

        # データを指定のフォーマットに整形(コンマ区切り)
        data = f"{word}"

        # UDPソケットを作成
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(data.encode("utf-8"), (host, port))
    
    if key & 0xFF == ord('f'):
        print("r")
        # UDPで送信
        host = "localhost"
        port = 5001

        # データを指定のフォーマットに整形(コンマ区切り)
        data = f"{script}"

        # UDPソケットを作成
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(data.encode("utf-8"), (host, port))

    if key & 0xFF == 27:  # Esc
        break

cv2.destroyAllWindows()  # ウィンドウを閉じる