# Full Stack Trivia API Backend


## The documantations are in :
https://documenter.getpostman.com/view/7646139/SW7c2n18

## The frontend had build from the begining with Svelte Js !!!
to activate svelte app:
```bash
npm install
npm run dev
```


## the collection , testing and the docs have build like the methods described in that course :
https://www.udemy.com/course/advanced-rest-apis-flask-python

## The tests are included in the postman file (you could load it from this repo). 
### trivia-udacity.postman_collection.json

you can run the all the tests with the "runner" button 
on the top of the postman app.

## virtual environment has created with pipenv.

to install and activate the pipfile :

```bash
$ pipenv install 
$ pipenv shell
```
## the trivia.psql have been changed to work with pg-admin 4. 
before it worked just with psql terminal.


## Running the server

To run the server, execute:

```bash
export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```

or :
```bash
python run.py
```

## errors handlers :
I used mainly custom error messages. 
But i did two error handlers for the exercise.

## questions per page declared in the config file.