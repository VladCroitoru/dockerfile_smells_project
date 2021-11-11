FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential python-software-properties libssl-dev libffi-dev git nodejs npm
RUN pip install --upgrade pip
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
#expose whatever port you configured in config.yaml
EXPOSE 11000
ENTRYPOINT python runserver.py