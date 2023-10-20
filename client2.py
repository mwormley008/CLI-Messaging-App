import socket 
import time
import os
import platform 
import threading


class Client:  # Class names in Python are typically CamelCase
    '''Node for sending request to server to initiate communication'''

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            # self.server_host = input('Enter server hostname (provided by ngrok): ')
            self.server_host = '8.tcp.ngrok.io'
            # The port used here is the standard for HTTPS connections, as ngrok uses it.
            self.server_port = 11168  # This is the default port that Ngrok uses for its secure tunnel
            if not self.server_host:
                continue
            break
        print('Finding connection')
        time.sleep(1)

    def make_connection(self):
        '''Sending connection request to the server node'''
        while True:
            try:
                server = (self.server_host, self.server_port)
                self.client_socket.connect(server)
                print('Connection successful made to the server')
                return True
            except:
                print('Retrying connection...')
                time.sleep(2)  # Changed to a longer sleep time for practical reasons

    def send_sms(self, msg):
        '''Sending the message to the connected server'''    
        self.client_socket.send(msg.encode())

    def receive_sms(self):
        '''Receiving message from the server'''
        while True:
            data = self.client_socket.recv(1024).decode()
            time.sleep(0.001)
            print(data)  # Printing messages received from the server

    def chat_room(self):
        if self.make_connection():
            receiving_thread = threading.Thread(target=self.receive_sms)
            receiving_thread.daemon = True
            receiving_thread.start()

            while True:    
                message = input()
                formatted_message = "\nclient:{}\n".format(message)
                self.send_sms(formatted_message)

if __name__ == '__main__':
    client_instance = Client()
    client_instance.chat_room()
