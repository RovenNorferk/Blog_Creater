# Blog Application

A simple blog application built with a FastAPI backend, Streamlit frontend, and MySQL database. The app allows users to create accounts, post content, view and delete posts, and manage data through a relational database. The project is fully dockerized for easy deployment and portability.

## Features

- **User Management**: Create, view, and manage users with timestamps for creation and updates.
- **Post Management**: Create, view, and delete posts associated with users, with timestamps and foreign key relationships to ensure data integrity.
- **Database Integration**: Uses MySQL with SQLAlchemy for ORM and Alembic for migrations, ensuring schema consistency.
- **API**: FastAPI provides a RESTful API with automatic Swagger UI documentation for testing endpoints.
- **Frontend**: Streamlit offers a user-friendly interface for interacting with the API.
- **Dockerization**: The project is containerized with separate services for the database, backend, and frontend, making it easy to run and deploy.

## Technologies Used

- **Backend**: FastAPI (for API development) and SQLAlchemy (for database ORM).
- **Frontend**: Streamlit (for interactive UI).
- **Database**: MySQL (relational database with tables for users and posts, including timestamps and foreign keys).
- **Migrations**: Alembic (for managing database schema changes).
- **Containerization**: Docker and Docker Compose (for multi-service orchestration).
- **Other**: Pydantic for data validation, PyMySQL for MySQL driver, Requests for frontend-backend communication.

## Installation and Setup

### Prerequisites

- Python 3.12 or higher.
- Docker Desktop (for containerization).
- MySQL (for local development, if not using Docker).

### Local Setup (Without Docker)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ashishaditya/blog-application.git
   cd blog-application
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # On Windows
   # OR
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - Start your local MySQL server and create the `blog_application` database.
   - Update `.env` with your database URL:
     ```
     DATABASE_URL=mysql+pymysql://root:myorcriss@localhost:3306/blog_application
     ```

5. **Run migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Start the backend:**
   ```bash
   uvicorn main:app --reload
   ```

7. **Start the frontend:**
   ```bash
   streamlit run streamlit_app.py
   ```

8. **Access the app:**
   - Frontend: [http://localhost:8501](http://localhost:8501)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

### Docker Setup (Recommended)

The project is dockerized with separate containers for the database (MySQL), backend (FastAPI), and frontend (Streamlit).

1. **Ensure Docker is installed and running.**

2. **Start the services:**
   ```bash
   docker-compose up --build
   ```

3. **Access the app:**
   - Frontend: [http://localhost:8501](http://localhost:8501)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)

4. **Stop the services:**
   ```bash
   docker-compose down -v
   ```

### Docker Hub Images

The Docker images for the backend and frontend are available on Docker Hub:

- **Backend**: [ashishaditya/blog-backend](https://hub.docker.com/r/ashishaditya/blog-backend)
- **Frontend**: [ashishaditya/blog-frontend](https://hub.docker.com/r/ashishaditya/blog-frontend)

## Database Schema

The application uses SQL (MySQL) for data persistence. Key tables:

- **users**: Stores user information with `id` (primary key), `username` (unique), `created_at`, and `updated_at`.
- **posts**: Stores posts with `id` (primary key), `title`, `content`, `user_id` (foreign key to `users.id`), `created_at`, and `updated_at`.

Migrations are handled by Alembic, ensuring schema evolution (e.g., adding timestamps and foreign keys).

## API Endpoints (FastAPI)

The backend provides CRUD operations:

- `POST /users/`: Create a user.
- `GET /users/{user_id}`: View a user.
- `POST /posts/`: Create a post.
- `GET /posts/{post_id}`: View a post.
- `DELETE /posts/{post_id}`: Delete a post.

Test endpoints using the Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs).

## Frontend (Streamlit)

The frontend provides a simple interface for user and post management:

- Create/View/Delete users and posts.
- Displays timestamps for creation and updates.

## Screenshots

### Streamlit Frontend
![Streamlit Frontend](Frontend-Streamlit.png)

### FastAPI Swagger UI (API Documentation)
![FastAPI Swagger UI](Backend-API.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Fork the repository and submit a pull request with improvements. For major changes, open an issue first to discuss.

---

**Note**: Replace the screenshot URLs with your actual image links. You can upload them to a service like [Imgur](https://imgur.com/) or add them to a `/screenshots` folder in your GitHub repo and link them as `![Streamlit Frontend](screenshots/streamlit.png)`.
