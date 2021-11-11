FROM openjdk:11-jre-slim-buster

ENV username=admin
ENV password=pw

RUN export client_id
RUN export client_secret
RUN export redirect_uri
RUN export url_auth

# Installation of dependencies
RUN apt-get update && apt-get upgrade -y
RUN apt-get install grep procps -y
RUN apt-get install python3.7 python3-pip -y
RUN apt-get install default-mysql-server -y
RUN apt-get install default-libmysqlclient-dev python-dev -y

RUN pip3 install virtualenv

# Copy essential files to docker env
COPY fuseki/ /app/fuseki
COPY INCIPIT_CRIS/ /app/INCIPIT_CRIS
COPY schema_ontology/ /app/schema_ontology
COPY INCIPIT-CRIS_docker_launcher.sh /app/INCIPIT-CRIS_docker_launcher.sh
COPY requirements.txt /app/requirements.txt

WORKDIR /app

EXPOSE 8000

CMD ./INCIPIT-CRIS_docker_launcher.sh