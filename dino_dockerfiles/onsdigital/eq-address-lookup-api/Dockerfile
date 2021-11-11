FROM python:3.6

RUN pip install pipenv==8.2.7 \
  && pip install gunicorn==19.7.1 \
  && pip install gevent==1.2.2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV AWS_DEFAULT_REGION eu-west-1

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

EXPOSE 6030

ENTRYPOINT ["sh", "docker-entrypoint.sh"]

COPY . /usr/src/app
