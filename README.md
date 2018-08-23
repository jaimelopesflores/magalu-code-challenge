# Luizalabs Employee Manager

This challenge solves the "growing team" problem from Luizalabs.

## General

**Tech Stack/Dependencies**
* vim 8.0
* git 2.17.1
* python 2.7.10
* pip 18.0
* virtualenv 16.0.0
* django 1.11.15
* flask 1.0.2
* docker 18.03.1-ce
* docker-compose 1.21.1
* 


**Pre-setup to development environment**

This project require a MongoDB instance. Setup one with the command below:
```bash
docker run -d -p 27017:27017 --name mongo mongo
```

Git clone the repo and go to project directory:
```bash
git clone git@github.com:jaimelopesflores/magalu-code-challenge.git
cd magalu-code-challenge
```

**Env files**

Can be found in _./service/env_files/_ and _./frontend/env_files/_

**Microservices dependencies**

Can be found in _./service/requirements.txt_ and _./frontend/requirements.txt_

## Service

Is an entity-based microservice in Flask that provide an employee syncronous api.

### Running the microservice

Go to directory _services_ from the repo root:
```bash
cd service
```

Install the virtual enrironment with _virtualenv_:
```bash
virtualenv env
```

Then install the _service_ dependencies:
```bash
env/bin/pip install -r requirements.txt
```

Finally, run the application:
```bash
FLASK_ENV=development env/bin/python run.py
```

The application will be running in [localhost:8000](http://localhost:8000)

### Endpoints

> GET [/employee](http://localhost:8000/employee) - _Retrieve an employee list_

> GET [/employee/:id](http://localhost:8000/employee/:id) - _Retrieve an employee by id_

> POST [/employee](http://localhost:8000/employee) - _Create a new employee_

> PUT [/employee/:id](http://localhost:8000/employee/:id) - _Update an employee_

> DELETE [/employee/:id](http://localhost:8000/employee/:id) - _Delete an employee_

#### POST and PUT Body Schema
```json
{
    "name": "<string>",
    "email": "<string>",
    "department": "<string>"
}

```

#### POST and PUT Header
```python
'Content-Type': 'application/json'
```

### Test

There are only 2 blackbox unit tests, just to prove the concept (TDD was not applied in this code).
The test also up a MongoDB docker container, once it's a dependency of the project.

To run the tests, run the following command:

```bash
FLASK_ENV=test env/bin/nosetests
```

### Containirize and run

```bash
docker build -t service .
docker run -d -p 8000:8000 --name service service
```

## Frontend

Is a frontend microservice in Django that provides the "Luizalabs Employee Manager" interface.

### Running the microservice

Go to directory _frontend_ from the repo root:
```bash
cd frontend
```

Install the virtual enrironment with _virtualenv_:
```bash
virtualenv env
```

Then install the _frontend_ dependencies:
```bash
env/bin/pip install -r requirements.txt
```

Finally, run the application:
```bash
DJANGO_ENV=development env/bin/python manage.py runserver 8001
```

Access the management portal in [http://localhost:8001/employees](http://localhost:8001/employees) and play with the CRUD operations.


### Containirize and run

```bash
docker build -t frontend .
docker run -d -p 8001:8001 --name frontend frontend
```

## Composing up



All this projects can be set up and running using docker-compose, but first you may stop the _mongo_, _service_ and _frontend_ containers because of port forwarding conflicts.
```bash
docker stop mongo service frontend
```

From the repo root, run the command below.
```bash
docker-compose up
````

The command above will build the microservices and run the microservices along with a MongoDB instance.

## Improvements

I understand the proposal of a code-challenge is to prove the concepts of the candidate, and because of this most of the times not all the best pratices in software development are applied.

There is a list of initial improvements that can be made.

### Tests
Tests are indispensable if you want to have a stable and reliable microservice. In this project only 2 unit tests were implemented. The test suite must cover almost all the code of an app to be almost totally sensitive to changes.

### Logging
The logging is being done with _print_s in this project. For a good monitoring, rich logs are essential.

### Security
I did not implemented security at all (Django has a built-in security module). At the least for the service api some JWT or Basic Auth validation should be implemented.

### Modularization
A microservice is not necessarily micro in features. Once the application grows, an improved architecture should be adopted.

### Configuration managament
The configurations are being done through env files. This is not a bad pratice at all when you do not have a large microservices ecosystem. The picture change when you have to have your ecosystem in a high availability environment where you can scale indeterminately. The best choice in this cases is to have a configuration server.

### API docs
Must be generated automatically with a framework like Swagger for example. Any change reflect in the docs by itself.

### Schema validation
We have a body validation in POST and PUT request to the service api. Can be improved with regexes (for the e-mail for example).
Validations for the path parameters are also needed.

### Docker imagege size improvement
The Docker images must be improved in size (using multi-stage build) and uptime for a performatic scale.