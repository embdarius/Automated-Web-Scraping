def start_server():
    host = '127.0.0.1'
    port = 65432  # Port to listen on

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}...")

    while True:
        conn, addr = server_socket.accept()  # Accept new client connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()  # Start a new thread for each client
        print(f"Active connections: {threading.active_count() - 2}")    # -2 because 1 thread for program, 1 thread for scrape_thread
