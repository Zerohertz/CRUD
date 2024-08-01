## Init

<!-- markdownlint-disable -->

```sh
$ spring init --language=java --javaVersion=17 --dependencies=web,data-jpa,postgresql --type=gradle-project --groupId=xyz.zerohertz --artifactId=crud --name=crud app
Using service at https://start.spring.io
Project extracted to '/home/zerohertz/workspace/Java-SpringBoot/app'
```

<!-- markdownlint-enable -->

## Run

<!-- markdownlint-disable -->

```sh
# ./gradlew bootRun
$ ./gradlew build
$ java -jar build/libs/crud-0.0.1-SNAPSHOT.jar --server.port=1547
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.3.2)
2024-08-01T15:07:07.040+09:00  INFO 12978 --- [crud] [           main] xyz.zerohertz.crud.CrudApplication       : Starting CrudApplication v0.0.1-SNAPSHOT using Java 17.0.11 with PID 12978 (/home/zerohertz/workspace/Java-SpringBoot/app/build/libs/crud-0.0.1-SNAPSHOT.jar started by zerohertz in /home/zerohertz/workspace/Java-SpringBoot/app)
...
```

<!-- markdownlint-enable -->

## Logs

> Server

```java
2024-08-01T15:10:48.245+09:00  INFO 13152 --- [crud] [nio-1547-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-08-01T15:10:48.245+09:00  INFO 13152 --- [crud] [nio-1547-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-08-01T15:10:48.246+09:00  INFO 13152 --- [crud] [nio-1547-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 0 ms
Hibernate: insert into users (created_at,email,password,updated_at,username) values (?,?,?,?,?) returning id
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0 where u1_0.id=?
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0 where u1_0.id=?
Hibernate: update users set email=?,password=?,updated_at=?,username=? where id=?
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0 where u1_0.id=?
Hibernate: update users set email=?,password=?,updated_at=?,username=? where id=?
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0 where u1_0.id=?
Hibernate: delete from users where id=?
Hibernate: select u1_0.id,u1_0.created_at,u1_0.email,u1_0.password,u1_0.updated_at,u1_0.username from users u1_0
```

> Client

```python
[08/01/24 15:10:48] INFO     [CLIENT] Create User Response: 201                                                                                                   client.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt':
                             '2024-08-01T15:10:48.353379', 'updatedAt': '2024-08-01T15:10:48.353495'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt':
                             '2024-08-01T15:10:48.353379', 'updatedAt': '2024-08-01T15:10:48.353495'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                              client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt':
                             '2024-08-01T15:10:48.353379', 'updatedAt': '2024-08-01T15:10:48.353495'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                 client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'password': 'securepassword123',
                             'createdAt': '2024-08-01T15:10:48.353379', 'updatedAt': '2024-08-01T15:10:48.538918'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                         client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': '{"email": "john.newemail@example.com"}', 'password':
                             'securepassword123', 'createdAt': '2024-08-01T15:10:48.353379', 'updatedAt': '2024-08-01T15:10:48.566625'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                 client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                 client.py:26
                                     []
```
