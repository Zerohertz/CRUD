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

```python
[07/30/24 09:40:37] INFO     [CLIENT] Create User Response: 201                                                                                                      cli.py:19
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T00:40:37.240114Z', 'updated_at':
                             None}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                    cli.py:25
                                     [{'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T00:40:37.240114Z', 'updated_at':
                             None}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                 cli.py:32
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'id': 1, 'created_at': '2024-07-30T00:40:37.240114Z', 'updated_at':
                             None}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                    cli.py:42
                                     {'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'id': 1, 'created_at': '2024-07-30T00:40:37.240114Z',
                             'updated_at': '2024-07-30T00:40:37.322272Z'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                            cli.py:52
                                     {'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'id': 1, 'created_at': '2024-07-30T00:40:37.240114Z',
                             'updated_at': '2024-07-30T00:40:37.343059Z'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                    cli.py:60
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                    cli.py:25
                                     []
```
