import socket, threading

def handle_client(client_socket, password):
    pass

def start_server():
    address = ('localhost', 2024)
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(address)
    server_sock.listen()
    