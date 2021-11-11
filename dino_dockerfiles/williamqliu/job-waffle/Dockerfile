### Get packages and updates for our base image
FROM ubuntu:14.04
MAINTAINER William Liu "william.q.liu@gmail.com"
ENV REFRESHED_AT 2015-03-14

# --yes to automatically answer 'y' when prompted 'Do you want to continue [y/N]'
# --force-yes when it asks for a manual confirmation if the package signature owner
# key isn't in the keyring
RUN apt-get update && apt-get --yes --force-yes install \
    git-core \
    gunicorn \
    libpq-dev \
    nginx \
    python-dev \
    python-setuptools \
    supervisor

RUN easy_install pip

RUN mkdir /opt/job-waffle
WORKDIR /opt/job-waffle
RUN (cd /opt/job-waffle && sudo git init)
RUN (cd /opt/job-waffle && sudo git remote add origin https://github.com/WilliamQLiu/job-waffle.git)
RUN (cd /opt/job-waffle && sudo git pull origin master)
RUN (cd /opt/job-waffle && pip install -r requirements.txt)
ADD . /opt/job-waffle/
#CMD ["python", "manage.py", "migrate", "--noinput"]
#CMD ["python", "manage.py", "collectstatic", "--noinput"]

EXPOSE 8000
