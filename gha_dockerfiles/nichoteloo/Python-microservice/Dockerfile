FROM python:3.8
ENV PYTHONBUFFERED=1
WORKDIR /django
COPY requirements.txt /django/requirements.txt
RUN pip3 install -r requirements.txt
COPY . .