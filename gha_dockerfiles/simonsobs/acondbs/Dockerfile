FROM python:3.9.7

WORKDIR /app

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y sqlite3

RUN pip install --upgrade pip
COPY ./ acondbs
RUN pip install ./acondbs/
RUN pip install gunicorn

ENV FLASK_APP "acondbs:create_app('/app/acondbs/docker/config.py')"

CMD [ "/app/acondbs/docker/cmd.sh" ]
