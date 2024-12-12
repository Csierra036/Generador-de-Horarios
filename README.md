# Generador-de-Horarios

Requerimientos Técnico:
* Python: Versión 3.11
* PostgreSQL: Version 17.2

## Instalacion

### 1. Pipenv
Comprobamos la versión de python y pip
```bash
python --version
pip --version
```
Instalamos Pipenv
```bash
pip install pipenv --user
```
Agregamos al PATH
Ejecutamos
```bash
python -m site --user-site
```
Reemplazamos site-packages con Scripts en el retorno. Por lo que agregaríamos al PATH una ruta parecida a : "C:\Users\Username\AppData\Roaming\Python37\Scripts"

### 2. Configuramos el ambiente virtual
- Crea un archivo `.env` basado en `.env.example`. Todas las variables de entorno son obligatorias.

### 3. Instalamos dependencias
```bash
  pyenv local 3.11
  pipenv --python 3.11
  pipenv install
  pip install alembic fastapi psycopg2-binary pydantic sqlalchemy uvicorn
```
### 4. Ejecutamos el proyecto
```bash
  pipenv run start 
  http://localhost:8000/docs
```
