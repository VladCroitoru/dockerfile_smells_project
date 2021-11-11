FROM python:3

ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ./entrypoint.sh
