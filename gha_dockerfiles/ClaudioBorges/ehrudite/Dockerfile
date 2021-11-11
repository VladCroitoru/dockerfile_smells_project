FROM ubuntu 

COPY ./input-data/ /tmp/ehrudite/
RUN apt-get update && apt-get -y install python python3-pip git

RUN git clone https://github.com/ClaudioBorges/ehrpreper /tmp/ehrpreper
WORKDIR /tmp/ehrpreper
RUN python3 setup.py install
RUN rm -rf /tmp/ehrpreper

RUN mkdir -p /usr/share/ehrudite
RUN ehrpreper -i /tmp/ehrudite/mimicIII/ -o /usr/share/ehrudite/prepared.xml -x mimicIII -vvv
RUN rm -rf /tmp/ehrudite
