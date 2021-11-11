FROM ubuntu:latest
MAINTAINER thibaut.mottet@gmail.com


RUN mkdir /workspace
WORKDIR /workspace
RUN apt-get update 
RUN apt-get install -y wget unzip ffmpeg
RUN wget https://github.com/inAudible-NG/tables/archive/master.zip
RUN unzip master.zip && rm master.zip
RUN mv tables-master/* .
RUN wget https://github.com/KrumpetPirate/AAXtoMP3/archive/master.zip
RUN unzip master.zip && rm master.zip
RUN mv AAXtoMP3-master/* .

CMD ["bash"]
