## Run

```sh
$ uvicorn app.main:app --host 0.0.0.0 --port 1547
INFO:     Started server process [54903]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:1547 (Press CTRL+C to quit)
```

## Logs

> Server

```python
INFO:     192.168.219.1:49931 - "POST /users HTTP/1.1" 201 Created
INFO:     192.168.219.1:49932 - "GET /users HTTP/1.1" 200 OK
INFO:     192.168.219.1:49933 - "GET /users/1 HTTP/1.1" 200 OK
INFO:     192.168.219.1:49934 - "PUT /users/1 HTTP/1.1" 200 OK
INFO:     192.168.219.1:49935 - "PATCH /users/1 HTTP/1.1" 200 OK
INFO:     192.168.219.1:49936 - "DELETE /users/1 HTTP/1.1" 204 No Content
INFO:     192.168.219.1:49937 - "GET /users HTTP/1.1" 200 OK
```

> Client

```python
[08/01/24 20:48:38] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-08-01T11:48:38.613337Z', 'updated_at': None}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-08-01T11:48:38.613337Z', 'updated_at': None}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-08-01T11:48:38.613337Z', 'updated_at': None}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'id': 1, 'created_at': '2024-08-01T11:48:38.613337Z', 'updated_at': '2024-08-01T11:48:38.683208Z'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'id': 1, 'created_at': '2024-08-01T11:48:38.613337Z', 'updated_at': '2024-08-01T11:48:38.698686Z'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
