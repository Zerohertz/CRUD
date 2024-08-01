## Init

```sh
$ go mod init app
go: creating new go.mod: module app
$ go get -u github.com/gin-gonic/gin

$ go get -u gorm.io/gorm
$ go get -u gorm.io/driver/postgres
```

## Run

```sh
$ go build main.go
go: downloading github.com/gin-gonic/gin v1.10.0
...
go: downloading github.com/go-playground/locales v0.14.1
$ ./main
...
[GIN-debug] POST   /users                    --> app/handlers.(*UserHandler).CreateUser-fm (3 handlers)
[GIN-debug] GET    /users                    --> app/handlers.(*UserHandler).GetAllUsers-fm (3 handlers)
[GIN-debug] GET    /users/:id                --> app/handlers.(*UserHandler).GetUserByID-fm (3 handlers)
[GIN-debug] PUT    /users/:id                --> app/handlers.(*UserHandler).UpdateUser-fm (3 handlers)
[GIN-debug] PATCH  /users/:id                --> app/handlers.(*UserHandler).PartiallyUpdateUser-fm (3 handlers)
[GIN-debug] DELETE /users/:id                --> app/handlers.(*UserHandler).DeleteUser-fm (3 handlers)
[GIN-debug] [WARNING] You trusted all proxies, this is NOT safe. We recommend you to set a value.
Please check https://pkg.go.dev/github.com/gin-gonic/gin#readme-don-t-trust-all-proxies for details.
[GIN-debug] Listening and serving HTTP on :1547
```

```sh
$ go run main.go
...
[GIN-debug] POST   /users                    --> app/handlers.(*UserHandler).CreateUser-fm (3 handlers)
[GIN-debug] GET    /users                    --> app/handlers.(*UserHandler).GetAllUsers-fm (3 handlers)
[GIN-debug] GET    /users/:id                --> app/handlers.(*UserHandler).GetUserByID-fm (3 handlers)
[GIN-debug] PUT    /users/:id                --> app/handlers.(*UserHandler).UpdateUser-fm (3 handlers)
[GIN-debug] PATCH  /users/:id                --> app/handlers.(*UserHandler).PartiallyUpdateUser-fm (3 handlers)
[GIN-debug] DELETE /users/:id                --> app/handlers.(*UserHandler).DeleteUser-fm (3 handlers)
[GIN-debug] [WARNING] You trusted all proxies, this is NOT safe. We recommend you to set a value.
Please check https://pkg.go.dev/github.com/gin-gonic/gin#readme-don-t-trust-all-proxies for details.
[GIN-debug] Listening and serving HTTP on :1547
```

## Logs

> Server

```go
[GIN] 2024/08/01 - 20:45:15 | 201 |    4.663389ms |   192.168.219.1 | POST     "/users"
[GIN] 2024/08/01 - 20:45:15 | 200 |     437.536µs |   192.168.219.1 | GET      "/users"
[GIN] 2024/08/01 - 20:45:15 | 200 |     948.662µs |   192.168.219.1 | GET      "/users/1"
[GIN] 2024/08/01 - 20:45:15 | 200 |    1.747551ms |   192.168.219.1 | PUT      "/users/1"
[GIN] 2024/08/01 - 20:45:15 | 200 |    1.522485ms |   192.168.219.1 | PATCH    "/users/1"
[GIN] 2024/08/01 - 20:45:15 | 204 |    1.371401ms |   192.168.219.1 | DELETE   "/users/1"
[GIN] 2024/08/01 - 20:45:15 | 200 |     237.949µs |   192.168.219.1 | GET      "/users"
```

> Client

```python
[08/01/24 20:45:15] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-08-01T20:45:15.356878+09:00', 'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-08-01T20:45:15.356878+09:00', 'updated_at': '0001-01-01T00:00:00Z'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'created_at': '2024-08-01T20:45:15.356878+09:00', 'updated_at': '0001-01-01T00:00:00Z'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'created_at': '2024-08-01T20:45:15.356878+09:00', 'updated_at': '2024-08-01T20:45:15.422422422+09:00'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'created_at': '2024-08-01T20:45:15.356878+09:00', 'updated_at': '2024-08-01T20:45:15.434930479+09:00'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
