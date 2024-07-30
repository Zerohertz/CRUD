## Init

<!-- markdownlint-disable -->

```sh
$ go mod init app
$ go get -u github.com/gin-gonic/gin
$ go get -u gorm.io/gorm
$ go get -u gorm.io/driver/postgres
```

<!-- markdownlint-enable -->

## Run

```sh
$ kubectl -n crud k8s
deployment.apps/gin created
configmap/postgres-config created
secret/postgres-secret created
deployment.apps/postgres created
service/postgres created
$ kubectl -n crud exec -it deploy/gin -- zsh
$ go run main.go
```

## Logs

> Server

```go
[GIN] 2024/07/30 - 10:45:28 | 201 |    3.023524ms | 000.000.000.000 | POST     "/users"
[GIN] 2024/07/30 - 10:45:28 | 200 |     531.935µs | 000.000.000.000 | GET      "/users"
[GIN] 2024/07/30 - 10:45:28 | 200 |      883.79µs | 000.000.000.000 | GET      "/users/1"
[GIN] 2024/07/30 - 10:45:28 | 200 |     1.78771ms | 000.000.000.000 | PUT      "/users/1"
[GIN] 2024/07/30 - 10:45:28 | 200 |    1.336857ms | 000.000.000.000 | PATCH    "/users/1"
[GIN] 2024/07/30 - 10:45:28 | 204 |    1.150564ms | 000.000.000.000 | DELETE   "/users/1"
[GIN] 2024/07/30 - 10:45:28 | 200 |     241.817µs | 000.000.000.000 | GET      "/users"
```

> Client

```python
[07/30/24 10:45:28] INFO     [CLIENT] Create User Response: 201                                                                                                   client.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:45:28.388524+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:45:28.388524+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                              client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:45:28.388524+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                 client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'created_at':
                             '2024-07-30T10:45:28.388524+09:00', 'updated_at': '2024-07-30T10:45:28.432954349+09:00'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                         client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'created_at':
                             '2024-07-30T10:45:28.388524+09:00', 'updated_at': '2024-07-30T10:45:28.447066674+09:00'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                 client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     []
```
