## Init

```sh
$ cargo new app --bin
    Creating binary (application) `app` package
note: see more `Cargo.toml` keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html
$ sudo apt-get update
$ sudo apt-get install -y libpq-dev
$ cargo install diesel_cli --no-default-features --features postgres
...
   Installed package `diesel_cli v2.2.1` (executable `diesel`)
$ echo "DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}" > .env
$ diesel setup
Creating migrations directory at: /home/zerohertz/workspace/Rust-ActixWeb/app/migrations
$ diesel migration generate create_users
Creating migrations/2024-08-01-111256_create_users/up.sql
Creating migrations/2024-08-01-111256_create_users/down.sql
$ diesel migration run
diesel migration run
Running migration 2024-08-01-111256_create_users
```

```sql
main=# \d users
                                        Table "public.users"
   Column   |            Type             | Collation | Nullable |              Default
------------+-----------------------------+-----------+----------+-----------------------------------
 id         | integer                     |           | not null | nextval('users_id_seq'::regclass)
 username   | character varying(50)       |           | not null |
 email      | character varying(100)      |           | not null |
 password   | character varying(255)      |           | not null |
 created_at | timestamp without time zone |           | not null | CURRENT_TIMESTAMP
 updated_at | timestamp without time zone |           |          |
Indexes:
    "users_pkey" PRIMARY KEY, btree (id)
    "users_email_key" UNIQUE CONSTRAINT, btree (email)
    "users_username_key" UNIQUE CONSTRAINT, btree (username)
```

## Run

```sh
$ cargo build
...
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 25.46s
$ target/debug/app
```

```sh
$ cargo run
   Compiling app v0.1.0 (/home/zerohertz/workspace/Rust-ActixWeb/app)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 2.71s
     Running `target/debug/app`
```

## Logs

> Server

```rust
...
```

> Client

```python
[08/01/24 20:41:20] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'id': 2, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01 11:41:20', 'updated_at': None}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'id': 2, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01 11:41:20', 'updated_at': None}]
                    INFO     [CLIENT] Get User by ID 2 Response: 200                                                                                                                                                                client.py:35
                                     {'id': 2, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01 11:41:20', 'updated_at': None}
                    INFO     [CLIENT] Update User 2 Response: 200                                                                                                                                                                   client.py:45
                                     {'id': 2, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01 11:41:20', 'updated_at': None}
                    INFO     [CLIENT] Partial Update User 2 Response: 200                                                                                                                                                           client.py:55
                                     {'id': 2, 'username': 'john_doe_updated', 'email': 'john.newemail@example.com', 'password': 'securepassword123', 'created_at': '2024-08-01 11:41:20', 'updated_at': None}
                    INFO     [CLIENT] Delete User 2 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
