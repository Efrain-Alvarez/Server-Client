import socket

def send_txt_file(file_path, server_address):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Read the file contents
        with open(file_path, 'rb') as file:
            file_contents = file.read()

        # Send file data to the server
        file_data = f"{file_path}|{file_contents.decode()}"
        client_socket.sendto(file_data.encode(), server_address)

        # Receive the response from the server
        response, _ = client_socket.recvfrom(1024)
        print("Server response:", response.decode())

    finally:
        # Close the socket when done
        client_socket.close()

if __name__ == "__main__":
    file_path = "test.txt"  # file name with in the directory
    server_address = ('192.168.4.25', 12345)  # Change this to the server's address and port

    send_txt_file(file_path, server_address)
