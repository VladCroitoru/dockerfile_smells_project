FROM python:3.9-alpine3.14
WORKDIR /src
ENV AWS_DEFAULT_REGION "ap-southeast-1"
ENV AWS_ENDPOINT_URL "ap-southeast-1.amazonaws.com"
COPY *.py .
COPY requirements.txt .
RUN apk update && apk upgrade --available
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "/src/main.py"]