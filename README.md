# book-management-service

## Book Management Service

- A classic book management system (a.k.a. library management) app
- It is an API backend service, which interacts with clients via REST API
- Building this app using Flask


## Personal Goals for this app

1. Build a fully functional API service using Flask
2. Serving these API endpoints - 
   - books:
     - POST /books - Add new book 
     - GET /books - Get all books 
     - GET /books/<book_id> - Get a specific book 
     - PUT /books/<book_id> - Modify an existing book 
     - DELETE /books/<book_id> - Delete an existing book 
   
   - reviews:
     - POST /books/<book_id>/reviews - Add a new review for a book 
     - GET /books/<book_id>/reviews - Get all the reviews for a book

   - users:
     - POST /users - Add a new user 
     - GET /users -Get a specific user 

3. Add authentication 
4. Use .env (python-dotenv) for storing creds 
5. Use Postgres DB 
6. Add unit tests
7. Dockerize the service 
8. Deploy on Render (want to try first)
9. Deploy on AWS 
10. Add logs 
11. Swagger doc 
12. Grafana metrics


## Steps to run in local

1. Clone this repo
2. Create a virtual environment in this project directory via terminal command -
    ```
    python3 -m venv venv
    ```
3. Activate this virtual environment -
    ```
    source venv/bin/activate
    ```
4. Install all the project requirements -
   ```
   pip install -r requirements
   ```
5. Create a `.env` file -
   ```
   SQLALCHEMY_DATABASE_URI=<YOUR_SQLITE_DB_URI>
   JWT_SECRET_KEY=<YOUR_JWT_SECRET_KEY>
   ```
6. Run the app service (default port: 8000) -
   ```
   /bin/bash run.sh
   ```
