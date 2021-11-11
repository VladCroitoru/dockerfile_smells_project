FROM python:3.9 as development

RUN mkdir /application
WORKDIR /application
COPY python-requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r python-requirements.txt

VOLUME /application

EXPOSE 8000

CMD ["/usr/local/bin/gunicorn", "-w 1", "-k geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "--certfile selfsigned-cert.pem", "--keyfile selfsigned-key.pem", "--reload", "--graceful-timeout 3600000", "--timeout 999999999", "--bind 0.0.0.0:8000", "flask_main:app"]

#Production only actions
FROM development as production

COPY app/ .
CMD ["/usr/local/bin/gunicorn", "-w 1", "-k geventwebsocket.gunicorn.workers.GeventWebSocketWorker", "--graceful-timeout 3600000", "--timeout 999999999", "--bind 0.0.0.0:8000", "flask_main:app"]