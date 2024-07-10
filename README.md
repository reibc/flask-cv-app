# HOW TO RUN

## Run from source
1) Install the dependencies using the command `pip install -r requirements.txt`
2) Update the cv_data.json in `app/data/cv_data.json` if needed
3) Launch the application by running `run.py`

## Run in Docker
1) Open cmd in the folder where Dockerfile is located (`flask-simple-cv-reader`)
2) Build the docker image by running the command `docker build -t flask-simple-cv-reader .`
3) Run the docker container `docker run -p 5000:5000 flask-simple-cv-reader`

# Usage

## API
* API routes are available on `localhost:/5000/swagger`

## Flask-CLI
* The following CLI commands are available:
    - `flask show experience {id}`
    - `flask show personal {id}`
    - `flask show education {id}`
    
    NOTE: Replace `{id}` with an integer matching the CV id from `cv_data.json`
