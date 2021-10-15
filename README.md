# Global API

## Configuración del Proyecto

### 1° Versión

- controllers
- env (entorno de python)
- files (se genera automáticamente)
- models
- schemas
- templates
- utils
- wsdl
- .env
- .gitignore
- application.py
- llave.key
- llave.pem
- config.py
- README.md
- requirements.txt
- routes.py

### 2° Versión

- env (entorno de python)
- files (se genera automáticamente)
- admin
  - auth
    - routes
    - controllers
    - models
    - schemas
  - accounting
- landing (por definirse)
  - kushki
  - sunat
- utils
- templates
- wsdl
- .env
- .gitignore
- application.py
- llave.key
- llave.pem
- config.py
- README.md
- requirements.txt

### 1. Crear el entorno virtual

```shell
  virtualenv env
```

### 2. Activar el entorno virtual

```shell
  source env/bin/activate
```

### 3. Instalar dependencias

```shell
  pip install -r requirements.txt
```

### 4. Crear archivo .env

Agregar credenciales de la base de datos

### 5. Ejecutar el programa

```shell
  python src/app.py
```

## Consultas básicas de SQLAlchemy

- Documentación de [SQLAlchemy](https://docs.sqlalchemy.org/en/14/tutorial/)

- Documentación de [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)

### Consultar (SELECT)

- Consultar todos los registros.

  ```python
    Model.query.all()
  ```

- Consultar con un límite los registros. Solo obtendrá los primeros 3 registros.

  ```python
    Model.query.limit(3).all()
  ```

- Consultar con una condición

  Para asegurarse de que solo devuelva un registro se puede usar el método first.

  ```python
    Model.query.filter(Model.field == some_value).first()
  ```

- Consultar con varias condiciones

  ```python
    Model.query.filter(Model.field1 == some_value1).(Model.field2 == some_value2).first()
  ```

### Crear (CREATE)

- Crear un registro

  ```python
    new_record = Model(value1, value2, value3, value4, ...)

    db.session.add(new_record)
    db.session.commit()
  ```

### Actualizar (UPDATE)

- Actualizar un registro

  ```python
    record = Model.query.filter(Model.field == some_value)

    record.field= new_value

    db.session.add(record)
    db.session.commit()
  ```

### Eliminar (DELETE)

- Eliminar un registro

  ```python
    record = Model.query.get(3)

    db.session.delete(record)
    db.session.commit()
  ```
