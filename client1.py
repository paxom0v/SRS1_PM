import socket
import threading

user_name = input("Здравствуйте, введите логин: ")
# Создаем клиентский сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12355))  # Подключаемся к серверу

# Функция для отправки сообщений серверу
def send_message():
    while True:
        start_message = input()
        if start_message == "/exit":
            client_socket.close()
            exit()
        else:
            message = user_name + ": " + start_message;
            client_socket.send(message.encode('utf-8'))

# Функция для приема сообщений от сервера
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("Ошибка приема сообщения")
            break

# Создаем отдельные потоки для отправки и приема сообщений
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()