## Run

```sh
$ gunicorn app.main:app --bind 0.0.0.0:1547
[2024-08-01 22:51:11 +0900] [1854] [INFO] Starting gunicorn 22.0.0
[2024-08-01 22:51:11 +0900] [1854] [INFO] Listening at: http://0.0.0.0:1547 (1854)
[2024-08-01 22:51:11 +0900] [1854] [INFO] Using worker: sync
[2024-08-01 22:51:11 +0900] [1855] [INFO] Booting worker with pid: 1855
```

## Logs

> Server

```python
...
```

> Client

```python
[08/01/24 22:51:40] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'created_at': '2024-08-01T13:51:40.276657', 'email': 'john.doe@example.com', 'id': 1, 'updated_at': None, 'username': 'john_doe'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'created_at': '2024-08-01T13:51:40.276657', 'email': 'john.doe@example.com', 'id': 1, 'updated_at': None, 'username': 'john_doe'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'created_at': '2024-08-01T13:51:40.276657', 'email': 'john.doe@example.com', 'id': 1, 'updated_at': None, 'username': 'john_doe'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'created_at': '2024-08-01T13:51:40.276657', 'email': 'john.doe.updated@example.com', 'id': 1, 'updated_at': '2024-08-01T13:51:40.336783', 'username': 'john_doe_updated'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'created_at': '2024-08-01T13:51:40.276657', 'email': 'john.newemail@example.com', 'id': 1, 'updated_at': '2024-08-01T13:51:40.354678', 'username': 'john_doe_updated'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
