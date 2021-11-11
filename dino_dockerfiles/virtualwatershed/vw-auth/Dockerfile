FROM ubuntu:14.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y git build-essential python-dev curl python-pip libpq-dev
RUN pip install -U pip
RUN apt-get install -y libssl-dev libffi-dev

RUN curl -sL https://deb.nodesource.com/setup_4.x | sh -
RUN apt-get install -y nodejs
RUN npm install -g bower

COPY . /var/www/vw-auth
WORKDIR /var/www/vw-auth

ENV VWAUTH_HOST 0.0.0.0
ENV VWAUTH_PORT 5000


ENV VWAUTH_SECRET vw-auth

ENV VWAUTH_SQLALCHEMY_DATABASE_URI sqlite:////dev.db

ENV VWAUTH_WTF_CSRF_ENABLED false
ENV VWAUTH_WTF_CSRF_CHECK_DEFAULT false


ENV VWAUTH_SECURITY_REGISTERABLE true
ENV VWAUTH_SECURITY_RECOVERABLE false
ENV VWAUTH_SECURITY_CONFIRMABLE false
ENV VWAUTH_SECURITY_PASSWORD_HASH sha512_crypt
ENV VWAUTH_SECURITY_PASSWORD_SALT add_salt
ENV VWAUTH_SECURITY_EMAIL_SENDER welcome@virtualwatershed.org
ENV VWAUTH_JWT_EXPIRATION_DELTA 1

RUN pip install -r requirements/dev.txt
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN bower install

EXPOSE ${VWAUTH_PORT}

CMD python manage.py runserver -h ${VWAUTH_HOST} -p ${VWAUTH_PORT}
