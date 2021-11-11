FROM python:3.3.6-alpine
EXPOSE 8082

MAINTAINER pfichtner "https://github.com/pfichtner"

RUN apk update 
RUN apk add git
RUN pip install cherrypy

WORKDIR /opt/
RUN git clone -b master https://github.com/pfichtner/KataTrainReservation.git
WORKDIR /opt/KataTrainReservation/booking_reference_service

CMD ["python3", "booking_reference_service.py"]
