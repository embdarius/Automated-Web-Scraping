    def fetch_data_from_server(self, page_number):
        """Fetch rows from the server by sending the page number."""
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(('127.0.0.1', 65432))

            client_socket.sendall(str(page_number).encode())
            data = client_socket.recv(16384).decode('utf-8')
            parsed_data = json.loads(data)

            fetch_received.clear()
            fetch_received.extend(parsed_data['rows'])

            client_socket.close()
            self.update_canvas()

        except Exception as e:
            print(f"Error: {e}")
