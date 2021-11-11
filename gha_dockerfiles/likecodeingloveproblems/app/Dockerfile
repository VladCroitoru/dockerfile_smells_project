# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 && PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . .