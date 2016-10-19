# py-microblog
Microblogging application from
[Ruby on Rails Tutorial, 3rd Edition](http://3rd-edition.railstutorial.org/)
implemented using `python` & [`flask`](http://flask.pocoo.org/).

### Development Setup
It is convenient to use virtual `python` environment for the application. `virtualenv` helps us in creating and managing virtual environments. Install `virtualenv` using `pip`, if not already installed:
```bash
$ pip install virtualenv
```

Virtual `python` environment is a directory & can be created anywhere. To create a virtual environment in current directory:
```bash
$ virtualenv env
```

Activate the created virtual environment:
```bash
$ source env/bin/activate
```

#### Install dependencies
Python package dependencies can be installed using:
```bash
$ pip install -r requirements.txt
```

#### Add new dependency
Use `pip-install` script in `./bin` directory to install new dependency. `pip-install` automatically saves the installed package as dependency in `requirements.txt`.
```bash
$ ./bin/pip-install <package-name>
```

### Run Server
Server can be run using:
```bash
$ python run.py
```

Server will be listening at [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Run Tests
```bash
$ lettuce tests/features
```
