FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y libmysqlclient-dev
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y netcat

WORKDIR /app
COPY . /app

RUN chmod +x wait.sh
RUN pip install -r requirements.txt

CMD ./wait.sh && python app.py

EXPOSE 5000

