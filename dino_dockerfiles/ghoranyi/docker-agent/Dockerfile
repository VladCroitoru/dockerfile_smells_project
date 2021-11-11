FROM python:2.7.12-alpine



RUN apk update && apk add py-virtualenv
RUN virtualenv /virtualenv

ADD requirements.txt /app/requirements.txt
RUN /virtualenv/bin/pip install -r /app/requirements.txt

ADD . /app

CMD /virtualenv/bin/python /app/agent.py
