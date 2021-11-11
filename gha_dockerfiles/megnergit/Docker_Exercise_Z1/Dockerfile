# base image
FROM postgres:latest

# install python3
RUN apt-get update 
RUN apt-get -y install python3 python3-pip 
RUN apt-get -y install postgresql-server-dev-10

# create working directory
RUN mkdir -p /zep
WORKDIR /zep
COPY requirements.txt /zep/

# install dependency
RUN pip3 install -r requirements.txt

# change user
# USER postgres

# environmental variable 
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=PostgreSQL
ENV POSTGRES_DB=db_zeppelin

# copy python code
COPY currency_conversion.py /zep/


