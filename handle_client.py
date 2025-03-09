# LOGIC FOR HANDLING CLIENTS CONNECTING TO THE SERVER
def handle_client(conn, addr):
    print(f"New connection from {addr}")
    while True:
        try:
            data = conn.recv(1024).decode()  # Receive data (page number) from the client
            if not data:
                break
            print(f"Client {addr} requested page: {data}")

            # Fetch data from the PostgreSQL database using the connection pool
            page_number = int(data)
            limit = 20
            offset = (page_number - 1) * limit
            #query = f"SELECT * FROM test1 ORDER BY id DESC LIMIT {limit} OFFSET {offset}"
            query = f"SELECT * FROM test2 ORDER BY id DESC LIMIT {limit} OFFSET {offset}"

            # Get a connection from the pool
            conn_db = connection_pool.getconn()
            cursor = conn_db.cursor()

            cursor.execute(query)
            rows = cursor.fetchall()  # Fetch rows based on the query

            # Prepare the response data
            #response = f"Fetched {len(rows)} rows: {rows}"
            #print("Response is: " + str(response))

            response = {
                "status" : "success",
                "row_count" : len(rows),
                "rows" : rows
            }
            print("Response is : " + str(response))

            response_json = json.dumps(response)

            print("Response_json is: " + str(response_json))

            # Return the connection to the pool
            connection_pool.putconn(conn_db)

            # Send the fetched rows back to the client
            #conn.sendall(response.encode())
            conn.sendall(response_json.encode('utf-8'))

        except ConnectionResetError:
            break  # Handle a client disconnecting abruptly
        except ValueError:
            conn.sendall("Invalid page number. Please send a valid integer.".encode())
    print(f"Client {addr} disconnected.")
    conn.close()
