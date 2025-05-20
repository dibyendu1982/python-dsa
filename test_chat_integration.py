import unittest
import subprocess
import time
import socket
import json
import threading
import sys
import os

class TestChatIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up Docker container before running tests"""
        cls.container_id = None
        cls.server_port = 5000
        
        try:
            # Build the Docker image
            print("Building Docker image...")
            subprocess.run(
                ["docker", "build", "-t", "chat-app-test", "."],
                check=True,
                capture_output=True,
                text=True
            )
            print("Docker image built successfully")
            
            # Run the container
            print("Starting Docker container...")
            result = subprocess.run(
                [
                    "docker", "run",
                    "-d",  # detached mode
                    "-p", f"{cls.server_port}:{cls.server_port}",  # port mapping
                    "chat-app-test"
                ],
                check=True,
                capture_output=True,
                text=True
            )
            cls.container_id = result.stdout.strip()
            print(f"Container started with ID: {cls.container_id}")
            
            # Wait for server to start
            time.sleep(2)
            
        except subprocess.CalledProcessError as e:
            print(f"Error setting up test environment:")
            print(f"Command output: {e.output}")
            print(f"Command stderr: {e.stderr}")
            raise
    
    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        if cls.container_id:
            print("Stopping Docker container...")
            try:
                subprocess.run(
                    ["docker", "stop", cls.container_id],
                    check=True,
                    capture_output=True
                )
                subprocess.run(
                    ["docker", "rm", cls.container_id],
                    check=True,
                    capture_output=True
                )
                print("Container stopped and removed")
            except subprocess.CalledProcessError as e:
                print(f"Error cleaning up container: {e}")
    
    def test_client_connection(self):
        """Test basic client connection"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Attempting to connect to server...")
            client_socket.connect(('localhost', self.server_port))
            print("Connected to server")
            
            # Send client name and receive welcome message
            client_socket.send("TestClient".encode())
            response = client_socket.recv(1024).decode()
            data = json.loads(response)
            
            self.assertEqual(data["status"], "connected")
            self.assertEqual(data["message"], "Welcome TestClient!")
            print("Connection test successful")
            
        except Exception as e:
            print(f"Connection error: {e}")
            self.fail(f"Client connection failed: {e}")
        finally:
            client_socket.close()
    
    def test_message_exchange(self):
        """Test message exchange between two clients"""
        # Create two client sockets
        client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            print("Connecting clients...")
            # Connect both clients
            client1.connect(('localhost', self.server_port))
            client2.connect(('localhost', self.server_port))
            print("Both clients connected")
            
            # Send client names and receive welcome messages
            client1.send("Client1".encode())
            client2.send("Client2".encode())
            
            # Receive welcome messages
            welcome1 = json.loads(client1.recv(1024).decode())
            welcome2 = json.loads(client2.recv(1024).decode())
            
            self.assertEqual(welcome1["status"], "connected")
            self.assertEqual(welcome2["status"], "connected")
            
            # Send message from client1 to client2
            message = {
                "to": "Client2",
                "message": "Hello from Client1"
            }
            print("Sending message...")
            client1.send(json.dumps(message).encode())
            
            # Receive delivery confirmation on client1
            confirm = json.loads(client1.recv(1024).decode())
            self.assertEqual(confirm["status"], "sent")
            
            # Receive message on client2
            received = json.loads(client2.recv(1024).decode())
            
            self.assertEqual(received["from"], "Client1")
            self.assertEqual(received["message"], "Hello from Client1")
            print("Message exchange successful")
            
        except Exception as e:
            print(f"Message exchange error: {e}")
            self.fail(f"Message exchange failed: {e}")
        finally:
            client1.close()
            client2.close()
    
    def test_invalid_recipient(self):
        """Test sending message to non-existent recipient"""
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            print("Testing invalid recipient...")
            client_socket.connect(('localhost', self.server_port))
            client_socket.send("TestClient".encode())
            
            # Receive welcome message
            welcome = json.loads(client_socket.recv(1024).decode())
            self.assertEqual(welcome["status"], "connected")
            
            # Send message to non-existent recipient
            message = {
                "to": "NonExistentClient",
                "message": "Hello"
            }
            client_socket.send(json.dumps(message).encode())
            
            # Receive error response
            response = json.loads(client_socket.recv(1024).decode())
            
            self.assertIn("error", response)
            self.assertIn("NonExistentClient", response["error"])
            print("Invalid recipient test successful")
            
        except Exception as e:
            print(f"Invalid recipient test error: {e}")
            self.fail(f"Invalid recipient test failed: {e}")
        finally:
            client_socket.close()

if __name__ == '__main__':
    unittest.main() 