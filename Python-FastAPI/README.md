## Run

```sh
$ kubectl -n crud k8s
deployment.apps/fastapi created
configmap/postgres-config created
secret/postgres-secret created
deployment.apps/postgres created
service/postgres created
$ kubectl -n crud exec -it deploy/fastapi -- zsh
$ uvicorn app.main:app --host 0.0.0.0
```

## Logs

> Server

```python
INFO:     000.000.000.000:58678 - "POST /users HTTP/1.1" 201 Created
INFO:     000.000.000.000:58679 - "GET /users HTTP/1.1" 200 OK
INFO:     000.000.000.000:58680 - "GET /users/1 HTTP/1.1" 200 OK
INFO:     000.000.000.000:58681 - "PUT /users/1 HTTP/1.1" 200 OK
INFO:     000.000.000.000:58682 - "PATCH /users/1 HTTP/1.1" 200 OK
INFO:     000.000.000.000:58683 - "DELETE /users/1 HTTP/1.1" 204 No Content
INFO:     000.000.000.000:58684 - "GET /users HTTP/1.1" 200 OK
```

> Client

```python
[07/30/24 10:42:31] INFO     [CLIENT] Create User Response: 201                                                                                                   client.py:19
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T01:42:31.541608Z',
                             'updated_at': None}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     [{'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T01:42:31.541608Z',
                             'updated_at': None}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                              client.py:35
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T01:42:31.541608Z',
                             'updated_at': None}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                 client.py:45
                                     {'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'id': 1, 'created_at':
                             '2024-07-30T01:42:31.541608Z', 'updated_at': '2024-07-30T01:42:31.616406Z'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                         client.py:55
                                     {'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'id': 1, 'created_at': '2024-07-30T01:42:31.541608Z',
                             'updated_at': '2024-07-30T01:42:31.639244Z'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                 client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     []
```
