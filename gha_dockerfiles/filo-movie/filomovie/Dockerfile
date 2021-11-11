# Create a ubuntu base image with python 3 installed.
FROM ubuntu:18.04

# updates package list
RUN apt-get -y update

# Set home dir
ENV HOME /root

# Set the working directory
WORKDIR /

# copy all the files
COPY . .

# save requirements to temp folder so docker can find it
# COPY ../requirements.txt /tmp/requirements.txt


# Install dependencies
RUN apt-get update && apt-get install -y python3 python3-pip libpq-dev gcc
RUN pip3 install -r requirements.txt
RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8
RUN export FLASK_APP=filomovie

# Expose the required port
EXPOSE 5000


#Run the command
# CMD gunicorn main:app
#CMD flask run
CMD python3 app.py
