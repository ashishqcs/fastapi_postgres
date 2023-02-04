# fastapi_postgres
Python service using FastApi and Postgres db

### Pre-Requisites
* Python 3.9+
* Poetry 1.3+

### Run Application
* Run docker compose
  ```shell
    docker-compose up -d
    ```
* Enter venv
  ```shell
    poetry shell
    ```
* Start app
    ```shell
    make dev-env
    ```

### Dev Notes
* Create a new migration file using 
    ```bash 
    alembic revision -m <migration name>
    ```