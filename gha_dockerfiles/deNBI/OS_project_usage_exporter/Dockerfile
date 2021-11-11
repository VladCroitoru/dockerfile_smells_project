FROM python:3.9.6-alpine

RUN apk add --no-cache linux-headers musl-dev gcc libffi-dev openssl-dev cargo
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code

EXPOSE 8080
CMD ["python", "project_usage_exporter.py"]
