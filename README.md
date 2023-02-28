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

### Debug Application
* Create debug/run configuration from your IDE for app/main.py
* Set relevant poetry venv.
* Set parameters as `Python: Current File (Integrated Terminal)`
* Run/Debug app with ide

### Dev Notes
* Create a new migration file using 
    ```shell 
    alembic revision -m <migration name>
    ```
    for initializing alembic with async db
    ```shell
    alembic init -t async migrations
    ```
