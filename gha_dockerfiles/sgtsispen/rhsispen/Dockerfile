# base image
FROM python:3.8-slim

# environment for python logging
# send output to terminal without buffer
ENV PYTHONBUFFERED 1

# make workdir in container
# and copy current directory contents to workdir
RUN mkdir /app
WORKDIR /app
ADD . /app

# install needed packages
RUN apt-get update -y \
    && apt-get install -y default-libmysqlclient-dev build-essential 

#install requirements
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VITUAL_ENV/bin:$PATH"
#install python
RUN python3 -m venv /opt/venv
COPY requirements.txt .
RUN . /opt/venv/bin/activate && pip install --trusted-host pypi.python.org -r requirements.txt

#RUN pip install --trusted-host pypi.python.org -r requirements.txt 
 
# install dependences
RUN apt-get update -y \
    && apt-get install -y nano \
    && apt-get install -y git 

#inicializar o env
ENV VIRTUAL_ENV=/opt/venv 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt install -y libpangocairo-1.0-0
RUN apt install -y libcairo2-dev
