pyramid-todo
============

<img width="1151" alt="pyramid_todo" src="https://user-images.githubusercontent.com/36563045/82798453-7fe0e080-9eb3-11ea-858e-37f09aceacd4.png">


Getting Started
---------------

- Change directory into your newly created project.

  ```
  cd project
  ```

- Create a Python virtual environment.

  ```
  python3 -m venv env
  ```

- Upgrade packaging tools.

  ```
  env/bin/pip install --upgrade pip setuptools
  ```

- Install the project in editable mode with its testing requirements.
  ```
  env/bin/pip install poetry
  env/bin/poetry install
  ```

- Initialize and upgrade the database using Alembic.

    - Generate your first revision.
        ```
        env/bin/alembic -c development.ini revision --autogenerate -m "init"
        ```

    - Upgrade to that revision.
        ```
        env/bin/alembic -c development.ini upgrade head
        ```

- Load default data into the database using a script.
    ```
    env/bin/initialize_src_db development.ini
    ```

- Run your project's tests.
    ```
    env/bin/pytest
    ```

- Run your project.
    ```
    env/bin/pserve development.ini
    ```


- Or you can start with Docker.
    ```
    make build
    ```

    ```
    make run
    ```
