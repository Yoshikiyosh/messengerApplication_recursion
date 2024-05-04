import socket
from faker import Faker

def server_program():
    host = '127.0.0.1'  # サーバーのIPアドレス
    port = 5000  # 使用するポート

    server_socket = socket.socket()  # ソケットオブジェクトを作成
    server_socket.bind((host, port))  # サーバーを指定したポートにバインド
    server_socket.listen(2)  # 接続を受け入れる

    print("Waiting for connection...")
    conn, address = server_socket.accept()  # クライアントからの接続を受け入れる
    print("Connection from: " + str(address))

    fake = Faker()  # Fakerオブジェクトを作成

    while True:
        data = conn.recv(1024).decode()  # クライアントからのデータを受信
        if not data:
            break

        print("from connected user: " + str(data))

        # 偽のデータを生成してクライアントに送信
        response = fake.sentence()
        conn.send(response.encode())

    conn.close()  # 接続を閉じる

if __name__ == '__main__':
    server_program()
