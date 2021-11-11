FROM python:2.7
MAINTAINER marcbperez@users.noreply.github.com

EXPOSE 5000

ADD . /home/runner
WORKDIR /home/runner

ENV FLASK_APP="restfuloauth2"

RUN pip install -e .
CMD flask run --host=0.0.0.0
