# set base image (host OS)
FROM python:3.9.7-alpine3.14

# set the working directory in the container
WORKDIR /usr/src/

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN apk add build-base openldap-dev
RUN pip install --no-cache-dir -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .
