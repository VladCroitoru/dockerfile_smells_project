FROM python:3.5

EXPOSE 9000

RUN pip install autobahn

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python", "server.py"]