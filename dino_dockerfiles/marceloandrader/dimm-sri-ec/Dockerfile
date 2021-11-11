FROM java:8-jre
LABEL maintainer "marcelo.andrade.r@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y 
RUN apt-get install -y --force-yes --no-install-recommends \
   -o Dpkg::Options::="--force-confdef" \
   -o Dpkg::Options::="--force-confold" \
   wget \
   unzip

# link from http://www.sri.gob.ec/web/10138/665
#  Programa DIMM Formularios genérico (17.9 MB) fecha de actualización 03-02-2017
RUN wget --no-check-certificate "http://descargas.sri.gob.ec/download/declaraciones/DIMM_2018_01/GENERICO/dimmFormularios4J-1.9.zip"

RUN unzip dimmFormularios4J-1.9.zip -d /opt/dimm

RUN rm dimmFormularios4J-1.9.zip

RUN chmod +x /opt/dimm/dimmFormularios4JUnix.sh
# Remove & to execute in background
RUN sed -i s/\&// /opt/dimm/dimmFormularios4JUnix.sh

CMD /opt/dimm/dimmFormularios4JUnix.sh
