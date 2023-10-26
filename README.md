# tkinter-mouse-tracking

## 使い方

1. UDPを受信するローカルサーバーを立てる。  

```sh
python server.py
```

2. 別のターミナルを開き、送信用のアプリを立ち上げる。  

```sh
python main.py
```

3. 開いたGUIの上でマウスカーソルを遷移させると座標と各円の中ににマウスカーソルが入っているかどうかをUDPでローカルサーバー宛に送信。  
4. ローカルサーバーを立てたターミナルに`X,Y,Bitmask`が表示される。  

## 送信データフォーマット

X座標、Y座標、各円にマウスカーソルが入っているかどうかのビットマスクをコンマ区切りにしたもの。  

(例)

```txt
0.96,0.27,0000
0.94,0.27,0000
0.91,0.26,0000
0.90,0.26,0000
0.87,0.26,0000
0.85,0.26,0000
0.84,0.26,0000
0.82,0.26,0000
0.81,0.26,0000
0.79,0.26,0000
0.77,0.26,0000
0.76,0.26,0000
0.74,0.26,0000
0.73,0.26,0000
0.71,0.26,0000
0.70,0.26,0000
0.68,0.26,0000
0.66,0.26,0000
0.65,0.26,0000
0.63,0.26,0000
0.60,0.26,0000
0.58,0.26,0000
0.57,0.26,0000
0.55,0.26,0000
0.52,0.26,0001
0.50,0.26,0001
0.48,0.26,0001
0.47,0.26,0001
0.47,0.26,0001
0.45,0.26,0000
0.45,0.26,0000
0.44,0.26,0000
0.43,0.26,0000
0.43,0.25,0000
0.43,0.25,0000
0.43,0.25,0000
0.42,0.25,0000
0.42,0.25,0000
0.42,0.25,0000
0.42,0.26,0000
0.41,0.26,0000
0.41,0.28,0000
0.40,0.28,0000
0.40,0.29,0000
0.39,0.30,0000
0.38,0.32,0000
0.37,0.33,0000
0.36,0.33,0000
0.36,0.34,0000
0.35,0.35,0000
0.35,0.36,0000
0.34,0.36,0000
0.34,0.37,0000
0.34,0.37,0000
0.34,0.38,0000
0.34,0.38,0000
0.33,0.39,0000
0.33,0.40,0000
0.33,0.40,0000
0.33,0.41,0000
0.32,0.41,0000
0.32,0.41,0000
0.32,0.42,0000
0.32,0.42,0000
0.31,0.42,0000
0.31,0.42,0000
0.31,0.43,0000
0.31,0.43,0000
0.30,0.44,0000
0.30,0.45,0000
0.29,0.45,0000
0.29,0.46,0000
0.28,0.46,0000
0.28,0.47,0000
0.28,0.47,0010
0.28,0.48,0010
0.27,0.48,0010
0.27,0.48,0010
0.27,0.49,0010
0.26,0.49,0010
0.26,0.50,0010
0.26,0.50,0010
0.26,0.51,0010
0.26,0.51,0010
0.25,0.51,0010
0.25,0.51,0010
0.25,0.52,0010
0.25,0.52,0010
0.25,0.52,0010
0.25,0.53,0010
0.25,0.53,0010
0.25,0.53,0010
0.25,0.55,0000
0.26,0.55,0000
0.26,0.56,0000
0.26,0.56,0000
0.27,0.58,0000
0.28,0.59,0000
0.28,0.60,0000
0.29,0.61,0000
0.30,0.62,0000
0.30,0.63,0000
0.33,0.65,0000
0.34,0.67,0000
0.35,0.68,0000
0.36,0.69,0000
0.39,0.71,0000
0.40,0.71,0000
0.42,0.72,0000
0.43,0.72,0000
0.43,0.73,0000
0.44,0.73,0000
0.44,0.73,0000
0.44,0.73,0000
0.44,0.73,0000
0.45,0.73,0000
0.45,0.74,0000
0.46,0.74,0000
0.46,0.74,0000
0.47,0.74,1000
0.47,0.74,1000
0.47,0.74,1000
0.47,0.74,1000
0.47,0.75,1000
0.48,0.75,1000
0.48,0.75,1000
0.48,0.75,1000
0.49,0.75,1000
0.50,0.75,1000
0.50,0.75,1000
0.51,0.76,1000
0.51,0.76,1000
0.52,0.76,1000
0.52,0.76,1000
0.52,0.76,1000
0.52,0.76,1000
0.52,0.76,1000
0.53,0.75,1000
0.53,0.75,1000
0.53,0.75,1000
0.53,0.75,1000
0.53,0.74,1000
0.54,0.74,0000
0.55,0.72,0000
0.57,0.70,0000
0.57,0.69,0000
0.59,0.67,0000
0.61,0.65,0000
0.64,0.62,0000
0.67,0.60,0000
0.68,0.59,0000
0.70,0.57,0000
0.72,0.56,0000
0.73,0.55,0000
0.74,0.54,0000
0.75,0.54,0100
0.76,0.53,0100
0.77,0.52,0100
0.77,0.51,0100
0.78,0.51,0100
0.78,0.50,0100
0.80,0.49,0000
0.81,0.48,0000
0.81,0.47,0000
0.82,0.47,0000
0.82,0.47,0000
0.82,0.47,0000
0.82,0.47,0000
0.83,0.47,0000
0.84,0.47,0000
0.89,0.49,0000
0.91,0.50,0000
0.98,0.52,0000
```
