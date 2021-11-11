FROM docker.io/python:3.6.4-alpine3.7

LABEL maintainer="rob@fairwinds.com"
LABEL description="Waits for matching IAM role to be assigned"

COPY . .

RUN pip install -r requirements.txt

CMD python -u wait.py