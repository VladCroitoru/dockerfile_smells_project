FROM python:2.7.13-alpine

RUN apk update && apk add py-pip

RUN mkdir /workspace
WORKDIR /workspace

COPY lib lib
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]