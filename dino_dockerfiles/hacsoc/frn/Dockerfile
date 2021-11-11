FROM python:alpine
MAINTAINER Abdallah Soliman

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["gunicorn", "--workers=4", "wsgi", "-b", ":80"]
