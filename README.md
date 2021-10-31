# Platzi Task | Flask
> This project is part of the course "[Curso de Flask](https://platzi.com/cursos/flask/)" of [Platzi](https://platzi.com)

## Table of Contents:
- [Description](#description)
  - [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#run-it-locally)


## Description
This is project is a simple TODO App made with Flask for learning purposes.

### Features
- Blueprints
- Jinja2
- Bootstrap
- Firestore DB
- User Signup.
- User Login.
- CRUD of tasks.
- MyPY

## Requirements:
- Python >= 3.6

## Installation
1. Clone or download de repository:
    ```
    $ git clone https://github.com/JoseNoriegaa/platzi-task-app-flask
    ```

2. Open the console inside the project directory and create a virtual environment.
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

3. Install the app.
    ```bash
    (venv) $ pip install -r requirements.txt
    ```

4. Copy the `env.example` file into the same directory with the name `.env`
    ```bash
    $ cp ./env.example ./.env
    ```

5. Add the private key of the Firebase project in the root directory of the project with the following name.
    ```
    service-account.json
    ```

## Run it locally
The application will run on port 5000 by default.
```bash
$ flask run
```
