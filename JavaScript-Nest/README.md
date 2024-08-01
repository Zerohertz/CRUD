## Init

```sh
$ sudo npm install -g @nestjs/cli
$ nest new app
...
✔ Installation in progress... ☕
🚀  Successfully created project app
...
$ npm install @nestjs/config @nestjs/typeorm typeorm pg
$ nest generate module user
CREATE src/user/user.module.ts (81 bytes)
UPDATE src/app.module.ts (729 bytes)
$ nest generate service user
CREATE src/user/user.service.spec.ts (446 bytes)
CREATE src/user/user.service.ts (88 bytes)
UPDATE src/user/user.module.ts (155 bytes)
$ nest generate controller user
CREATE src/user/user.controller.spec.ts (478 bytes)
CREATE src/user/user.controller.ts (97 bytes)
UPDATE src/user/user.module.ts (240 bytes)
```

## Run

```sh
$ npm run start:dev
[10:30:52 PM] Starting compilation in watch mode...
[10:30:54 PM] Found 0 errors. Watching for file changes.
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [NestFactory] Starting Nest application...
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] AppModule dependencies initialized +22ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] TypeOrmModule dependencies initialized +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] ConfigHostModule dependencies initialized +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] ConfigModule dependencies initialized +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] TypeOrmCoreModule dependencies initialized +44ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] TypeOrmModule dependencies initialized +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [InstanceLoader] UserModule dependencies initialized +1ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RoutesResolver] UserController {/users}: +6ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users, POST} route +1ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users, GET} route +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users/:id, GET} route +1ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users/:id, PUT} route +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users/:id, PATCH} route +0ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [RouterExplorer] Mapped {/users/:id, DELETE} route +1ms
[Nest] 3294  - 08/01/2024, 10:30:54 PM     LOG [NestApplication] Nest application successfully started +1ms
```

## Logs

> Server

```javascript
...
```

> Client

```python
[08/01/24 22:32:03] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'updated_at': '2024-08-01T04:32:03.463Z', 'id': 1, 'created_at': '2024-08-01T04:32:03.463Z'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:32:03.463Z', 'updated_at': '2024-08-01T04:32:03.463Z'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:32:03.463Z', 'updated_at': '2024-08-01T04:32:03.463Z'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:32:03.463Z', 'updated_at':
                             '2024-08-01T04:32:03.518Z'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:32:03.463Z', 'updated_at':
                             '2024-08-01T04:32:03.537Z'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
