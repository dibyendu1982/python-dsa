import pytest
import subprocess
import time
import socket
import json
import os

@pytest.fixture(scope="session")
def docker_container():
    """Fixture to set up and tear down the Docker container"""
    container_id = None
    server_port = 5000
    
    # Build the Docker image
    print("\nBuilding Docker image...")
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
            "-p", f"{server_port}:{server_port}",  # port mapping
            "chat-app-test"
        ],
        check=True,
        capture_output=True,
        text=True
    )
    container_id = result.stdout.strip()
    print(f"Container started with ID: {container_id}")
    
    # Wait for server to start
    time.sleep(2)
    
    yield container_id, server_port
    
    # Cleanup
    print("\nStopping Docker container...")
    try:
        subprocess.run(
            ["docker", "stop", container_id],
            check=True,
            capture_output=True
        )
        subprocess.run(
            ["docker", "rm", container_id],
            check=True,
            capture_output=True
        )
        print("Container stopped and removed")
    except subprocess.CalledProcessError as e:
        print(f"Error cleaning up container: {e}")

@pytest.fixture
def client_socket(docker_container):
    """Fixture to create and clean up a client socket"""
    _, server_port = docker_container
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', server_port))
    yield sock
    sock.close()

def test_client_connection(client_socket):
    """Test basic client connection and welcome message"""
    # Send client name
    client_socket.send("TestClient".encode())
    
    # Receive welcome message
    response = client_socket.recv(1024).decode()
    data = json.loads(response)
    
    assert data["status"] == "connected"
    assert data["message"] == "Welcome TestClient!"

def test_message_exchange(docker_container):
    """Test message exchange between two clients"""
    _, server_port = docker_container
    
    # Create two client sockets
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect both clients
        client1.connect(('localhost', server_port))
        client2.connect(('localhost', server_port))
        
        # Send client names and receive welcome messages
        client1.send("Client1".encode())
        client2.send("Client2".encode())
        
        # Receive welcome messages
        welcome1 = json.loads(client1.recv(1024).decode())
        welcome2 = json.loads(client2.recv(1024).decode())
        
        assert welcome1["status"] == "connected"
        assert welcome2["status"] == "connected"
        
        # Send message from client1 to client2
        message = {
            "to": "Client2",
            "message": "Hello from Client1"
        }
        client1.send(json.dumps(message).encode())
        
        # Receive delivery confirmation on client1
        confirm = json.loads(client1.recv(1024).decode())
        assert confirm["status"] == "sent"
        
        # Receive message on client2
        received = json.loads(client2.recv(1024).decode())
        assert received["from"] == "Client1"
        assert received["message"] == "Hello from Client1"
        
    finally:
        client1.close()
        client2.close()

def test_invalid_recipient(client_socket):
    """Test sending message to non-existent recipient"""
    # Send client name and receive welcome message
    client_socket.send("TestClient".encode())
    welcome = json.loads(client_socket.recv(1024).decode())
    assert welcome["status"] == "connected"
    
    # Send message to non-existent recipient
    message = {
        "to": "NonExistentClient",
        "message": "Hello"
    }
    client_socket.send(json.dumps(message).encode())
    
    # Receive error response
    response = json.loads(client_socket.recv(1024).decode())
    assert "error" in response
    assert "NonExistentClient" in response["error"]

def test_invalid_message_format(client_socket):
    """Test sending invalid message format"""
    # Send client name and receive welcome message
    client_socket.send("TestClient".encode())
    welcome = json.loads(client_socket.recv(1024).decode())
    assert welcome["status"] == "connected"
    
    # Send invalid message format
    client_socket.send("not a json message".encode())
    
    # Receive error response
    response = json.loads(client_socket.recv(1024).decode())
    assert "error" in response
    assert "Invalid message format" in response["error"] 