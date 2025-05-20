# Socket Programming Concepts

## What is Socket Programming?

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.

## Socket Communication Diagram

```
+----------------+                    +----------------+
|  Client Socket |                    |  Server Socket |
+----------------+                    +----------------+
        |                                    |
        |           Network                  |
        |------------------------------------|
        |                                    |
        |                                    |
+----------------+                    +----------------+
|  Application   |                    |  Application   |
|  Layer         |                    |  Layer         |
+----------------+                    +----------------+
```

## Socket Module Functionality

The Python `socket` module provides low-level networking interface. Here are the key components:

### 1. Socket Creation
```python
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
- `AF_INET`: Address Family IPv4
- `SOCK_STREAM`: TCP socket type
- `SOCK_DGRAM`: UDP socket type

### 2. Server Socket Operations
```python
# Bind the socket to a specific address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections
server_socket.listen(5)

# Accept a connection
client_socket, address = server_socket.accept()
```

### 3. Client Socket Operations
```python
# Connect to the server
client_socket.connect(('localhost', 12345))
```

### 4. Data Transmission
```python
# Send data
client_socket.send(b'Hello, Server!')

# Receive data
data = client_socket.recv(1024)
```

### 5. Socket Closure
```python
# Close the socket
client_socket.close()
server_socket.close()
```

## Socket States

1. **CLOSED**: Initial state
2. **LISTEN**: Server is waiting for connections
3. **SYN_SENT**: Client has initiated connection
4. **SYN_RECEIVED**: Server has received SYN
5. **ESTABLISHED**: Connection is established
6. **CLOSE_WAIT**: Server received FIN from client
7. **LAST_ACK**: Server is waiting for final ACK
8. **FIN_WAIT_1**: Client initiated connection termination
9. **FIN_WAIT_2**: Client received ACK for its FIN
10. **CLOSING**: Both sides are trying to close simultaneously

## Common Socket Methods

- `socket()`: Creates a new socket
- `bind()`: Binds the socket to an address
- `listen()`: Enables a server to accept connections
- `accept()`: Accepts a connection
- `connect()`: Initiates a connection
- `send()`: Sends data
- `recv()`: Receives data
- `close()`: Closes the socket

## Error Handling

```python
try:
    # Socket operations
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    s.close()
```

## Best Practices

1. Always close sockets after use
2. Handle exceptions properly
3. Use appropriate buffer sizes
4. Implement proper error handling
5. Consider using context managers (`with` statement)
6. Use timeouts for blocking operations
7. Implement proper protocol for data exchange 