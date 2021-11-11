FROM python:2.7-alpine

COPY app /app

WORKDIR /app

RUN pip install boto3

CMD [ "python", "-u", "main.py" ]