# syntax=docker/dockerfile:1
FROM centos/python-38-centos7
WORKDIR /usr/src/docker-django
RUN pip3 install --upgrade setuptools pip

# FROM postgres
# FROM django:onbuild

# ENV POSTGRES_PASSWORD 123

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*

RUN yum update
RUN yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make libffi-devel
RUN yum -y install epel-release
RUN yum -y install python-pip
# RUN yum -y install python-devel python3-devel python-Levenshtein
RUN apt-get install -y python-apt
RUN apt-get install -y python3-pip
RUN apt-get install -y python-dev python3.7-dev python-levenshtein


RUN pip3 install tensorflow
RUN pip3 install tensorflow_datasets

COPY . .
RUN pip3 install -r requirements.txt

RUN pip3 install psycopg2-binary
RUN pip3 install websocket
RUN pip3 install websocket-client
RUN pip3 install zhconv
RUN pip3 install xlwt
RUN pip3 install django-import-export



EXPOSE 8000
CMD [ "python3", "manage.py", "runserver" ]

