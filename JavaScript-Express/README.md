## Init

```sh
$ npm init -y
Wrote to /home/zerohertz/Zerohertz/CRUD/JavaScript-Express/app/package.json:
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
$ npm install express pg dotenv body-parser
added 79 packages, and audited 80 packages in 6s
13 packages are looking for funding
  run `npm fund` for details
found 0 vulnerabilities
```

## Run

```sh
$ node server.js
Server is running on http://0.0.0.0:1547
Connected to the database
Users table created or already exists.
```

## Logs

> Server

```javascript
...
```

> Client

```python
[08/01/24 22:08:30] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:08:30.536Z', 'updated_at': None}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:08:30.536Z', 'updated_at': None}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:08:30.536Z', 'updated_at': None}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:08:30.536Z', 'updated_at':
                             '2024-08-01T04:08:30.580Z'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01T04:08:30.536Z', 'updated_at':
                             '2024-08-01T04:08:30.593Z'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
