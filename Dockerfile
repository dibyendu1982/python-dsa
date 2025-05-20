FROM python:3.9-slim

WORKDIR /app

# Copy the server and client files
COPY server.py client.py ./

# Expose the port that the server will run on
EXPOSE 5000

# Run the server
CMD ["python", "-u", "server.py"] 