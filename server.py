import socket
import struct
import os

def receive_file(server_socket, storage_directory):
    # Receive the filename length using 4 bytr messages
    # struct libary unpacks the recieved bytes and converts them to integers
    filename_length_bytes, client_address = server_socket.recvfrom(4)
    # ! means the byte order and the I means unsigned int
    # unpack is a tuple but we only want the signal element 
    filename_length = struct.unpack('!I', filename_length_bytes)[0]

    # Receive the filename
    filename_bytes, _ = server_socket.recvfrom(filename_length)
    file_name = filename_bytes.decode()

    # prints the ip and port 
    print(f"Received file '{file_name}' from {client_address}")

    # Receive file contents in 1024 chunks this can be changed but from what i read this is standard 
    file_contents, _ = server_socket.recvfrom(1024)

    # Determine the path to save the received file, storage path is set in the main fucntion
    file_path = os.path.join(storage_directory, file_name)

    # Save the received file
    with open(file_path, 'wb') as file:
        file.write(file_contents)

    # Send a response back to the client
    response = "File received successfully!"
    server_socket.sendto(response.encode(), client_address)

def start_udp_server(storage_directory):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('192.168.4.25', 12345)
    server_socket.bind(server_address)

    # Message to the terminal to let me know it is listening
    print("UDP server is listening on {}:{}".format(*server_address))

    while True:
        # Receive file data from the client
        receive_file(server_socket, storage_directory)

if __name__ == "__main__":
    storage_directory = "/home/efrainalvarez/Documents/Connection"  # Change this to the desired storage directory
    # Ensure the directory exists
    os.makedirs(storage_directory, exist_ok=True)  
    # Start the server, parameter passed is the path of directory you want to save the files in 
    start_udp_server(storage_directory)
