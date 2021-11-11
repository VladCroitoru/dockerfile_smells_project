FROM python:3

WORKDIR /app
COPY ./ .
RUN python setup.py install
ENTRYPOINT ["awstools"]
