import socket

def start_udp_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('192.168.4.25', 12345)
    server_socket.bind(server_address)

    print("UDP server is listening on {}:{}".format(*server_address))

    while True:
        # Receive file data from the client
        file_data, client_address = server_socket.recvfrom(1024)
        file_name, file_contents = file_data.decode().split('|', 1)

        print(f"Received file '{file_name}' from {client_address}")

        # Save the received file
        with open(file_name, 'wb') as file:
            file.write(file_contents.encode())

        # Send a response back to the client
        response = "File received successfully!"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_udp_server()
