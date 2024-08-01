## Init

```sh
$ spring init --language=java --javaVersion=17 --dependencies=web,data-jpa,postgresql --type=gradle-project --groupId=xyz.zerohertz --artifactId=crud --name=crud app
Using service at https://start.spring.io
Project extracted to '/home/zerohertz/workspace/Java-SpringBoot/app'
```

## Run

```sh
$ ./gradlew build
OpenJDK 64-Bit Server VM warning: Sharing is only supported for boot loader classes because bootstrap classpath has been appended
2024-08-01T21:03:54.338+09:00  INFO 56048 --- [crud] [ionShutdownHook] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence u
nit 'default'
2024-08-01T21:03:54.340+09:00  INFO 56048 --- [crud] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2024-08-01T21:03:54.343+09:00  INFO 56048 --- [crud] [ionShutdownHook] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.
BUILD SUCCESSFUL in 6s
7 actionable tasks: 7 executed
$ java -jar build/libs/crud-0.0.1-SNAPSHOT.jar --server.port=1547
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/

 :: Spring Boot ::                (v3.3.2)
2024-08-01T21:06:25.681+09:00  INFO 56146 --- [crud] [           main] xyz.zerohertz.crud.CrudApplication       : Starting CrudApplication v0.0.1-SNAPSHOT using Java 17.0.11 with PID 56146 (/home/zerohertz/workspace/Java-SpringBoot/app/build/libs/crud-0.0.1-SNAPSHOT.jar started by zerohertz in /home/zerohertz/workspace/Java-SpringBoot/app)
...
```

```sh
$ ./gradlew bootRun
...
Welcome to Gradle 8.8!
...
> Task :bootRun
  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.3.2)
2024-08-01T21:13:55.068+09:00  INFO 56575 --- [crud] [           main] xyz.zerohertz.crud.CrudApplication       : Starting CrudApplication using Java 17.0.11 with P
ID 56575 (/home/zerohertz/workspace/Java-SpringBoot/app/build/classes/java/main started by zerohertz in /home/zerohertz/workspace/Java-SpringBoot/app)
```

## Logs

> Server

```java
2024-08-01T21:07:15.890+09:00  INFO 56146 --- [crud] [nio-1547-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2024-08-01T21:07:15.890+09:00  INFO 56146 --- [crud] [nio-1547-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2024-08-01T21:07:15.891+09:00  INFO 56146 --- [crud] [nio-1547-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 1 ms
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
[08/01/24 21:07:16] INFO     [CLIENT] Create User Response: 201                                                                                                                                                                     client.py:19
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt': '2024-08-01T21:07:15.995014', 'updatedAt': '2024-08-01T21:07:15.995151'}
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     [{'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt': '2024-08-01T21:07:15.995014', 'updatedAt': '2024-08-01T21:07:15.995151'}]
                    INFO     [CLIENT] Get User by ID 1 Response: 200                                                                                                                                                                client.py:35
                                     {'id': 1, 'username': 'john_doe', 'email': 'john.doe@example.com', 'password': 'securepassword123', 'createdAt': '2024-08-01T21:07:15.995014', 'updatedAt': '2024-08-01T21:07:15.995151'}
                    INFO     [CLIENT] Update User 1 Response: 200                                                                                                                                                                   client.py:45
                                     {'id': 1, 'username': 'john_doe_updated', 'email': 'john.doe.updated@example.com', 'password': 'securepassword123', 'createdAt': '2024-08-01T21:07:15.995014', 'updatedAt':
                             '2024-08-01T21:07:16.209389'}
                    INFO     [CLIENT] Partial Update User 1 Response: 200                                                                                                                                                           client.py:55
                                     {'id': 1, 'username': 'john_doe_updated', 'email': '{"email": "john.newemail@example.com"}', 'password': 'securepassword123', 'createdAt': '2024-08-01T21:07:15.995014', 'updatedAt':
                             '2024-08-01T21:07:16.243491'}
                    INFO     [CLIENT] Delete User 1 Response: 204                                                                                                                                                                   client.py:63
                    INFO     [CLIENT] Get All Users Response: 200                                                                                                                                                                   client.py:26
                                     []
```
