from ubuntu:16.04

RUN apt-get update && apt-get install -y eatmydata
RUN apt-get update && eatmydata apt-get install -y build-essential git-core mpich

WORKDIR /opt

RUN git clone https://github.com/bluemix/mallba.git
RUN git clone https://github.com/themalvaproject/malva 

COPY mallba_environment /opt/mallba/environment
COPY malva_environment /opt/malva/environment

RUN cd /opt/mallba && make clean && make all
RUN cd /opt/malva && make clean && make all
