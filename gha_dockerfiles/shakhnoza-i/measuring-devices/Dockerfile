FROM ubuntu:20.04
# 1. running python in unbuffered mode which is recomended when running python within docker containers
ENV PYTHONUNBUFFERED 1 

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get -yq upgrade
RUN apt-get update
RUN apt-get -yq install libsnappy-dev graphviz graphviz-dev pkg-config
RUN apt-get install -yq build-essential libssl-dev libffi-dev python3-dev
RUN apt-get install -yq python3-setuptools
RUN apt-get install -yq python3-pip
RUN apt-get install -yq git mc postgresql-client 
RUN apt-get install -yq libxml2-dev libxslt1-dev 
RUN apt-get install -yq gdal-bin
RUN apt-get install -yq libgdal-dev


# 2. from out requirements.txt file copy to docker image file
COPY ./requirements.txt /requirements.txt
# the dependencies for psycopg2 to communicate between django and postgres
# RUN apt-get add --update --no-cache postgresql-client 
# # virtual - is it sets up an alias for our dependencies that we can use to easily remove all those dependencies later.
# RUN apt-get add --update --no-cache --virtual .tmp-build-deps \
#       gcc libc-dev linux-headers postgresql-dev
RUN pip3 install -r /requirements.txt 
# RUN apt-get del .tmp-build-deps

# 3. making directory within our Docker image that we can use to store our application source code
# a.creating directory
RUN mkdir /meter_project
# b.go to this directory
WORKDIR /meter_project
# c.copy our app folder from local machine to app folder we just created on docker image
COPY ./meter_project /meter_project

# 4. Creating app user - for security purposes, otherwise our app using the root account
# create user, -D means user runs on our application only and not having home directory
RUN adduser --no-create-home user
# switch docker to this user
USER user

# RUN chown nobody:nogroup "celerybeat-schedule"
# USER nobody
# CMD ["celery", "-A", "meter_project.celery_app", "-E", "-B"]