FROM python:3.8.2-buster
LABEL maintainer="Sandip Samal <sandip.samal@childrens.harvard.edu>"

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN apt update -y && apt-get install -y software-properties-common && \
    apt-add-repository 'deb http://security.debian.org/debian-security stretch/updates main' && apt update -y && \
    apt-get install -y openjdk-11-jdk-headless && \
    export JAVA_HOME && \
    apt-get clean

WORKDIR /usr/local/src

COPY java .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

# START WEBAPP SERVICE
CMD [ "hello_java","--help" ]

