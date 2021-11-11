FROM ubuntu

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:libreoffice/ppa
RUN apt-get update
RUN apt-get install -y --force-yes libreoffice
RUN apt-get clean

RUN ls /opt/

EXPOSE 8100
CMD soffice --headless --accept="socket,host=0.0.0.0,port=8100;urp;" --nofirststartwizard
