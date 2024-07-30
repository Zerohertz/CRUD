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
[GIN] 2024/07/30 - 10:35:23 | 201 |    3.302484ms | 121.134.174.157 | POST     "/users"
[GIN] 2024/07/30 - 10:35:23 | 200 |     656.922µs | 121.134.174.157 | GET      "/users"
[GIN] 2024/07/30 - 10:35:23 | 200 |     875.115µs | 121.134.174.157 | GET      "/users/1"
[GIN] 2024/07/30 - 10:35:23 | 200 |    1.526225ms | 121.134.174.157 | PUT      "/users/1"
[GIN] 2024/07/30 - 10:35:23 | 200 |    1.318683ms | 121.134.174.157 | PATCH    "/users/1"
[GIN] 2024/07/30 - 10:35:23 | 204 |    1.330195ms | 121.134.174.157 | DELETE   "/users/1"
[GIN] 2024/07/30 - 10:35:23 | 200 |     235.525µs | 121.134.174.157 | GET      "/users"
```

> Client

```python
[07/30/24 10:35:23] INFO     [CLIENT] Create User Response: 201                                                                                                      cli.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:35:23.499828+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                    cli.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:35:23.499828+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                 cli.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-07-30T10:35:23.499828+09:00',
                             'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                    cli.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'created_at':
                             '2024-07-30T10:35:23.499828+09:00', 'updated_at': '2024-07-30T10:35:23.540567908+09:00'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                            cli.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'created_at':
                             '2024-07-30T10:35:23.499828+09:00', 'updated_at': '2024-07-30T10:35:23.554918949+09:00'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                    cli.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                    cli.py:26
                                     []
```
