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
  ```commandline
    poetry shell
    ```
* Start app
    ```commandline
    make dev-env
    ```

### Dev Notes
* Create a new migration file using 
    ```shell 
    alembic revision -m <migration name>
    ```