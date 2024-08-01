<h1 align="center">🦀 CRUD 🦀</h1>

```sh
$ kubectl create ns crud
namespace/crud created
$ kubectl -n crud apply -f k8s
configmap/postgres-config created
secret/postgres-secret created
deployment.apps/postgres created
service/postgres created
deployment.apps/backend created
$ kubectl -n crud exec -it deploy/backend -- zsh
```

<h3 align="center">API Specification</h3>
<div align="center">
<img width="400" alt="crud" src="https://github.com/user-attachments/assets/a31ed9a1-7dfc-48b5-830e-f2fc112c9c02">

| Function              | Endpoint      | Method   | Description                                      | Request Headers                  | Request Body                                                                                        | Response                                                                                                                                                                                                                                                      |
| --------------------- | ------------- | -------- | ------------------------------------------------ | -------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create User           | `/users`      | `POST`   | Creates a new user.                              | `Content-Type: application/json` | `json { "username": "john_doe", "email": "john.doe@example.com", "password": "securepassword123" }` | Status: 201 Created<br>Body: `json { "id": "1", "username": "john_doe", "email": "john.doe@example.com", "created_at": "2024-07-30T12:34:56Z" }`                                                                                                              |
| Get All Users         | `/users`      | `GET`    | Retrieves all users.                             | -                                | -                                                                                                   | Status: 200 OK<br>Body: `json [ { "id": "1", "username": "john_doe", "email": "john.doe@example.com", "created_at": "2024-07-30T12:34:56Z" }, { "id": "2", "username": "jane_doe", "email": "jane.doe@example.com", "created_at": "2024-07-30T12:40:00Z" } ]` |
| Get User by ID        | `/users/{id}` | `GET`    | Retrieves a specific user by ID.                 | -                                | -                                                                                                   | Status: 200 OK<br>Body: `json { "id": "1", "username": "john_doe", "email": "john.doe@example.com", "created_at": "2024-07-30T12:34:56Z" }`                                                                                                                   |
| Update User           | `/users/{id}` | `PUT`    | Updates a specific user's information.           | `Content-Type: application/json` | `json { "username": "john_doe_updated", "email": "john.doe.updated@example.com" }`                  | Status: 200 OK<br>Body: `json { "id": "1", "username": "john_doe_updated", "email": "john.doe.updated@example.com", "updated_at": "2024-07-30T13:00:00Z" }`                                                                                                   |
| Partially Update User | `/users/{id}` | `PATCH`  | Partially updates a specific user's information. | `Content-Type: application/json` | `json { "email": "john.newemail@example.com" }`                                                     | Status: 200 OK<br>Body: `json { "id": "1", "username": "john_doe", "email": "john.newemail@example.com", "updated_at": "2024-07-30T13:30:00Z" }`                                                                                                              |
| Delete User           | `/users/{id}` | `DELETE` | Deletes a specific user.                         | -                                | -                                                                                                   | Status: 204<br>No Content                                                                                                                                                                                                                                     |

</div>

<h3 align="center">Database (PostgreSQL) Table Schema</h3>
<div align="center">

| Field      | Data Type    | Description        | Constraints                         |
| ---------- | ------------ | ------------------ | ----------------------------------- |
| id         | INT          | User's unique ID   | PRIMARY KEY, AUTO_INCREMENT         |
| username   | VARCHAR(50)  | User's username    | NOT NULL, UNIQUE                    |
| email      | VARCHAR(100) | User's email       | NOT NULL, UNIQUE                    |
| password   | VARCHAR(255) | User's password    | NOT NULL                            |
| created_at | DATETIME     | Creation timestamp | NOT NULL, DEFAULT CURRENT_TIMESTAMP |
| updated_at | DATETIME     | Update timestamp   | NULL, ON UPDATE CURRENT_TIMESTAMP   |

</div>
<div align="right">
    <code>DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}</code>
</div>
