# pull the official base image
FROM python:3.9.1

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV MONGODB_USERNAME=VedantPawar
ENV MONGODB_PASS=pbNGbZyyZ5QDp9Dk
ENV SECRET_KEY='250033e6422c0368a9c9ada6178476934e9927a75e9f07a4'

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]