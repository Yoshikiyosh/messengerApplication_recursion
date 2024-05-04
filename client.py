import socket

def client_program():
    host = '127.0.0.1'  # サーバーのIPアドレス
    port = 5000  # 使用するポート

    client_socket = socket.socket()  # ソケットオブジェクトを作成
    client_socket.connect((host, port))  # サーバーに接続

    message = input(" -> ")  # ユーザーからの入力を受け取る

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # サーバーにメッセージを送信
        data = client_socket.recv(1024).decode()  # サーバーからの応答を受信

        print('Received from server: ' + data)  # サーバーからの応答を表示

        message = input(" -> ")  # 再びユーザーからの入力を受け取る

    client_socket.close()  # ソケットを閉じる

if __name__ == '__main__':
    client_program()
