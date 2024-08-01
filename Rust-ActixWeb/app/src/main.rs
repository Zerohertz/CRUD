use actix_web::{web, App, HttpResponse, HttpServer, Result};
use diesel::prelude::*;
use diesel::r2d2::{self, ConnectionManager};
use dotenv::dotenv;
use std::env;

mod models;
mod schema;

type DbPool = r2d2::Pool<ConnectionManager<PgConnection>>;

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    dotenv().ok();

    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL must be set");
    let manager = ConnectionManager::<PgConnection>::new(database_url);
    let pool = r2d2::Pool::builder()
        .build(manager)
        .expect("Failed to create pool.");

    HttpServer::new(move || {
        App::new()
            .app_data(web::Data::new(pool.clone()))
            .service(
                web::resource("/users")
                    .route(web::get().to(get_all_users))
                    .route(web::post().to(create_user)),
            )
            .service(
                web::resource("/users/{id}")
                    .route(web::get().to(get_user))
                    .route(web::put().to(update_user))
                    .route(web::patch().to(partially_update_user))
                    .route(web::delete().to(delete_user)),
            )
    })
    .bind("0.0.0.0:1547")?
    .run()
    .await
}

async fn get_all_users(pool: web::Data<DbPool>) -> Result<HttpResponse> {
    use schema::users::dsl::*;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    let user_list = web::block(move || {
        let mut conn = conn; // Make conn mutable for load
        users.load::<models::User>(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(user_list))
}

async fn create_user(
    pool: web::Data<DbPool>,
    item: web::Json<models::NewUser>,
) -> Result<HttpResponse> {
    use schema::users;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    let new_user = models::NewUser {
        username: item.username.clone(),
        email: item.email.clone(),
        password: item.password.clone(),
    };

    let inserted_user = web::block(move || {
        let mut conn = conn; // Make conn mutable for get_result
        diesel::insert_into(users::table)
            .values(&new_user)
            .get_result::<models::User>(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::Created().json(inserted_user))
}

async fn get_user(pool: web::Data<DbPool>, user_id: web::Path<i32>) -> Result<HttpResponse> {
    use schema::users::dsl::*;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    let user = web::block(move || {
        let mut conn = conn; // Make conn mutable for first
        users
            .filter(id.eq(*user_id))
            .first::<models::User>(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(user))
}

async fn update_user(
    pool: web::Data<DbPool>,
    user_id: web::Path<i32>,
    item: web::Json<models::UpdateUser>,
) -> Result<HttpResponse> {
    use schema::users::dsl::*;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    let updated_user = web::block(move || {
        let mut conn = conn; // Make conn mutable for get_result
        diesel::update(users.filter(id.eq(*user_id)))
            .set(&*item)
            .get_result::<models::User>(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(updated_user))
}

async fn partially_update_user(
    pool: web::Data<DbPool>,
    user_id: web::Path<i32>,
    item: web::Json<models::UpdateUser>,
) -> Result<HttpResponse> {
    use schema::users::dsl::*;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    let partial_update = models::UpdateUser {
        username: item.username.clone(),
        email: item.email.clone(),
    };

    let updated_user = web::block(move || {
        let mut conn = conn; // Make conn mutable for get_result
        diesel::update(users.filter(id.eq(*user_id)))
            .set(&partial_update)
            .get_result::<models::User>(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::Ok().json(updated_user))
}

async fn delete_user(pool: web::Data<DbPool>, user_id: web::Path<i32>) -> Result<HttpResponse> {
    use schema::users::dsl::*;

    let conn = pool.get().expect("Couldn't get db connection from pool");

    web::block(move || {
        let mut conn = conn; // Make conn mutable for execute
        diesel::delete(users.filter(id.eq(*user_id))).execute(&mut conn)
    })
    .await?
    .map_err(actix_web::error::ErrorInternalServerError)?;

    Ok(HttpResponse::NoContent().finish())
}

