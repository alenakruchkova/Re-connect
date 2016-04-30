# Re-Connect
## Create repository:
git init

git remote add origin https://github.com/alenakruchkova/Re-connect.git

git add [a file]

git commit -m "[a message]"

git push -u origin master

## Devpost:

http://devpost.com/software/re-connect

## Run the stuff:

Run `virtualenv venv --distribute` 

Run `source venv/bin/activate`  Sets up and activates the virtual environment

Run `pip install -r requirements.txt`  Installs required files

Run the app `gunicorn app:app` Should run at 127.0.0.1:8000
