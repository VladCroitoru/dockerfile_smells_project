FROM python:2.7-alpine

RUN addgroup flask \
    && adduser -s /bin/sh -D -G flask flask

RUN mkdir -p /webapp

ADD requirements.txt /webapp
RUN pip install -r /webapp/requirements.txt

ADD . /webapp

RUN chown -R flask:flask /webapp

USER flask
WORKDIR /webapp

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["run.py"]
