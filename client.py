import socket
import threading
import json
import sys

class ChatClient:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.running = True
        
    def connect(self, name):
        try:
            self.client_socket.connect((self.host, self.port))
            # Send client name to server
            self.client_socket.send(name.encode())
            
            # Start receiving thread
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()
            
            print(f"Connected to server as {name}")
            print("Type 'quit' to exit")
            print("Format messages as: @recipient message")
            
            while self.running:
                message = input()
                if message.lower() == 'quit':
                    self.running = False
                    break
                    
                # Parse message format: @recipient message
                if message.startswith('@'):
                    try:
                        recipient, content = message[1:].split(' ', 1)
                        self.send_message(recipient, content)
                    except ValueError:
                        print("Invalid message format. Use: @recipient message")
                else:
                    print("Invalid message format. Use: @recipient message")
                    
        except Exception as e:
            print(f"Error connecting to server: {e}")
        finally:
            self.client_socket.close()
            
    def send_message(self, recipient, message):
        try:
            data = {
                "to": recipient,
                "message": message
            }
            self.client_socket.send(json.dumps(data).encode())
        except Exception as e:
            print(f"Error sending message: {e}")
            
    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                    
                data = json.loads(message)
                if "error" in data:
                    print(f"Error: {data['error']}")
                else:
                    print(f"\nFrom {data['from']}: {data['message']}")
                    
            except Exception as e:
                if self.running:
                    print(f"Error receiving message: {e}")
                break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python client.py <client_name>")
        sys.exit(1)
        
client = ChatClient()
client.connect(sys.argv[1]) 