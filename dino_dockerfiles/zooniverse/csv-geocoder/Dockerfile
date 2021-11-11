FROM python:2-alpine

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY geocode.py /usr/src/app

ENTRYPOINT [ "python", "geocode.py" ]
