import socket
import threading
import json

class ChatServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        self.clients = {}  # Dictionary to store client connections
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"New connection from {address}")
            
            # Start a new thread for each client
            client_thread = threading.Thread(
                target=self.handle_client,
                args=(client_socket,)
            )
            client_thread.start()
    
    def handle_client(self, client_socket):
        # Receive client's name
        try:
            client_name = client_socket.recv(1024).decode()
            self.clients[client_name] = client_socket
            print(f"{client_name} has joined the chat")
            
            # Send confirmation to client
            client_socket.send(
                json.dumps({
                    "status": "connected",
                    "message": f"Welcome {client_name}!"
                }).encode()
            )
            
            while True:
                # Receive message from client
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                    
                # Parse the message (expected format: {"to": "recipient", "message": "content"})
                try:
                    data = json.loads(message)
                    recipient = data.get("to")
                    message_content = data.get("message")
                    
                    if recipient in self.clients:
                        # Forward message to recipient
                        self.clients[recipient].send(
                            json.dumps({
                                "from": client_name,
                                "message": message_content
                            }).encode()
                        )
                        # Send confirmation to sender
                        client_socket.send(
                            json.dumps({
                                "status": "sent",
                                "to": recipient,
                                "message": message_content
                            }).encode()
                        )
                    else:
                        client_socket.send(
                            json.dumps({
                                "error": f"Recipient {recipient} not found"
                            }).encode()
                        )
                except json.JSONDecodeError:
                    client_socket.send(
                        json.dumps({
                            "error": "Invalid message format"
                        }).encode()
                    )
                    
        except Exception as e:
            print(f"Error handling client {client_name if 'client_name' in locals() else 'unknown'}: {e}")
        finally:
            # Clean up when client disconnects
            if 'client_name' in locals() and client_name in self.clients:
                del self.clients[client_name]
            client_socket.close()
            print(f"{client_name if 'client_name' in locals() else 'unknown'} has left the chat")

if __name__ == "__main__":
    server = ChatServer()
    server.start() 