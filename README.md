# Generador-de-Horarios

Requerimientos Técnico:
* Python: Versión 3.11

## Installation

Install project with pipenv the first:

### 1. Install Pipenv
https://pipenv.pypa.io/en/latest/installation.html

### 2. Set up environment
- Create an .env file based in .env.example. All environment variables are required..

### 3. Install dependencies
```bash
  pyenv local 3.11
  pipenv --python 3.11
  pipenv install
```
### 4. Running development project
```bash
  pipenv run start 
  http://localhost:8000/docs
```
### 5. Installing  FastAPI
```bash
  pipenv fastapi sqlalchemy psycopg2-binary
```
