FROM python:3.9 as backend
WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
