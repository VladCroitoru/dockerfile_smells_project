# This Dockerfile is used to build a aragorn python image
# starts with the python image
# creates a directory for the repo
# gets the aragorn repo
# and runs main which enables the gunicorn web server

FROM python:3.8.5

# get some credit
LABEL maintainer="powen@renci.org"

# install basic tools
RUN apt-get update

# make a directory for the repo
RUN mkdir /repo

# go to the directory where we are going to upload the repo
WORKDIR /repo

# get the latest code
RUN git clone https://github.com/ranking-agent/aragorn.git

# go to the repo dir
WORKDIR /repo/aragorn

# install requirements
RUN pip install -r requirements.txt

# expose the default port
EXPOSE 4868

# start the service entry point
ENTRYPOINT ["bash", "main.sh"]