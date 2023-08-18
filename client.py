import socket
import ssl
import tkinter as tk

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

        self.root = tk.Tk()
        self.root.geometry("1200x600")
        self.root.title("Random Quote Generator")
        self.label = tk.Label(self.root, text="Click the button to generate a random quote")
        self.label.pack(pady=10)
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.BOTTOM, pady=10)
        self.button = tk.Button(self.button_frame, text="Generate", command=self.generate_quote)
        self.button.pack(side=tk.LEFT, padx=10)

    def start(self):
        self.root.mainloop()

    def generate_quote(self):
        self.client_socket = self.ssl_context.wrap_socket(self.client_socket, server_hostname=self.host)
        self.client_socket.connect((self.host, self.port))
        self.client_socket.sendall(b"generate")
        quote = self.client_socket.recv(1024).decode()

        self.label.configure(text=quote)

        self.client_socket.close()
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if __name__ == '__main__':
    client = Client('localhost', 8080)
    client.start()
