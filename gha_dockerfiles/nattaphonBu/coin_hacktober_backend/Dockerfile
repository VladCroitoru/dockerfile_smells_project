
# python base image in the container from Docker Hub
FROM python:3.8

# copy files to the /app folder in the container
COPY . /app

# set the working directory in the container to be /app
WORKDIR /app

# install the packages from the Pipfile in the container
RUN  apt-get -y update
RUN  apt-get -y upgrade

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt

# expose the port that uvicorn will run the app on
CMD uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}