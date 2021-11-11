FROM continuumio/anaconda
RUN apt-get update -qq \
 && apt-get install gcc -y \
 && apt-get clean 

WORKDIR /setup/
COPY ./setup-cpu.sh .
#COPY ./ctpn /setup/ctpn
#RUN chmod 777 ./setup-cpu.sh
RUN sh ./setup-cpu.sh
#WORKDIR /setup/ctpn/lib/utils/
#RUN sh ./make-for-cpu.sh
WORKDIR /ocr/

