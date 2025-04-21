# Job Portal – GraphQL API in Python

This project is a **GraphQL API for a job portal**, built with Python using the **Graphene** library. It’s my first experience working with GraphQL, and I created this project as a hands-on way to learn the technology.

The API enables job listings, applications, user management, and role-based permissions—all exposed through a GraphQL interface using Graphene.

---

## Design and implementation

The main entities in the system are:

- **User** – Represents a person using the platform. Each user has a role (e.g., admin, employer, applicant) that determines permissions.
- **Employer** – A company or person who can create job listings.
- **Job** – A job posting created by an employer.
- **Job Application** – Represents an application submitted by a user for a specific job.

Some details on the implementation are:

- **GraphQL API with Graphene** – All operations are exposed as GraphQL queries and mutations.
- **SQLAlchemy** – Used as the ORM to interact with the PostgreSQL database.
- **Repository Pattern** – Abstracts data access from business logic to keep code maintainable.
- **Authentication with JWT tokens** – Login mutation returns a JWT token, which is used for authenticated requests via headers.
- **Authorization with decorators** – Custom decorators are used in queries and mutations to enforce role-based access (e.g., only allow admins or authenticated users to perform certain actions).

## Development Tools & Commands

### Setup

It’s recommended to use [`pyenv`](https://github.com/pyenv/pyenv) to manage your Python versions. To create a virtual environment:

```bash
# Install the required Python version
pyenv install 3.10

# Create a new virtual environment
pyenv virtualenv 3.10 job-portal

# Activate it
pyenv local job-portal
```

### Dependency Management
Dependencies and scripts are managed using Poetry. All dependencies are declared in [pyproject.toml](pyproject.toml).

```bash
# Install dependencies
poetry install

# Add a new package
poetry add <package-name>

# Add a dev dependency
poetry add --group dev <package-name>

# Update the lock file
poetry lock
```

### Running the Application

The application is fully containerized using **Docker** and Docker Compose (see [Docker compose file](docker-compose.yml)). It spins up:

- **Backend** – the GraphQL API service
- **PostgreSQL** – for data persistence
- **PGAdmin** – a web-based tool for managing PostgreSQL visually

```bash
# Build and start the services
docker-compose up -d

# Stop the services
docker-compose down

# View logs
docker-compose logs -f
```

The backend container uses a `prestart.sh` script as its entrypoint (see `Dockerfile`). This script:

- Applies all alembic migrations to the local database.
- Executes `init_db.py` to populate the database with initial data for local development.

### Code quality
[Tox](https://tox.readthedocs.io/) is configured to run multiple tools in isolated environments:

- **flake8** – Linting
- **black** – Formatting
- **mypy** – Static type checking

Run Tools with Tox:
```bash
# Run all tools
tox

# Run specific tool
tox -e flake8
tox -e black
tox -e mypy
```

### Database Migrations
Alembic is used for database version control and schema migrations.
```bash
# View current revision
docker-compose exec backend alembic history

# Create a new migration script (autogenerate schema changes)
docker-compose exec backend alembic revision --autogenerate -m "Migration message"

# Apply migrations to the database
docker-compose exec backend alembic upgrade head

# Downgrade to previous version (if needed)
docker-compose exec backend alembic downgrade <down revision ID>
```

---
## Acknowledgements

I followed the [Udemy course](https://www.udemy.com/course/building-graphql-apis-with-python/) titled **"Building GraphQL APIs with Python: Beginner To Pro"** as the foundation for the project. While the course helped me understand the basics, I extended the application with several features and specially configurations as well as best practices not covered in the course.

