FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt update && apt install git -y && apt install libgomp1 -y
RUN pip3 install -r requirements.txt && pip3 install git+https://github.com/Nicceboy/python-markdown-generator