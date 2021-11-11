FROM python:3.3.6-alpine
EXPOSE 8081

MAINTAINER pfichtner "https://github.com/pfichtner"

RUN apk update 
RUN apk add git
RUN pip install cherrypy

WORKDIR /opt/
RUN git clone -b master https://github.com/pfichtner/KataTrainReservation.git
WORKDIR /opt/KataTrainReservation/train_data_service

CMD ["python3", "start_service.py"]
