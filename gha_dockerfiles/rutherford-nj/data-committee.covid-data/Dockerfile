FROM python:3.8.12-slim-bullseye

# apt install needed packages
RUN apt update && yes | apt install curl mawk r-base sed

# install node for svgo
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt install -y nodejs

COPY requirements.txt /
RUN pip install -r /requirements.txt
