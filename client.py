import socket
import os
import struct

def send_file(file_path, server_address):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Get the file name from the path, does not include the path 
        file_name = os.path.basename(file_path)

        # Send filename length, ! means the order of the bytes and the I is unsigned int
        filename_length = len(file_name)
        client_socket.sendto(struct.pack('!I', filename_length), server_address)

        # Send the filename
        client_socket.sendto(file_name.encode(), server_address)

        # Read the file contents as binary
        with open(file_path, 'rb') as file:
            file_contents = file.read()

        # Send file contents to the server
        client_socket.sendto(file_contents, server_address)

        # Receive the response from the server
        response, _ = client_socket.recvfrom(1024)
        print("Server response:", response.decode())

    finally:
        # Close the socket when done
        client_socket.close()

if __name__ == "__main__":
    file_path = "test.txt"  # file name within the directory
    server_address = ('192.168.4.25', 12345)  # Change this to the server's address and port

    send_file(file_path, server_address)
