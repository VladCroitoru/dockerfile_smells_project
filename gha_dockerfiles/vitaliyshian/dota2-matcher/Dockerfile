#FROM ubuntu:16.04
#
#LABEL maintainer="vitaliy.shian@gmail.com"
## docker build -t dota2-matcher:latest .
## Обновление Ubuntu
#RUN apt-get update
#RUN apt-get -y upgrade
#
## Установка дополнительных библиотек для работы с инфроструктурой
#RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
#RUN apt-get install -y python3.9
#
## Проверка версии Python
#RUN python3 -V
#
## Установка пакетного менеджера pip
#RUN apt-get install -y python3-pip
#
#COPY ./requirements.txt /app/requirements.txt
#
#RUN pip3 install -r /app/requirements.txt
#
#COPY . /app
#
#ENTRYPOINT [ "python3" ]
#CMD [ "/app/main.py" ]

# Виртуальная машина Python
FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["main.py"]

ENTRYPOINT ["python3"]


