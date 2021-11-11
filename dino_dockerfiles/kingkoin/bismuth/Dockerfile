FROM ubuntu:16.04
MAINTAINER < twitter.com/king_koin >

ENV BISMUTH_WALLET=6a90e43ee72bde80b5bc92c0f397a564f8ccf192edcfbf9f2b27246c
ENV RIG_NAME=KINGSRIG

RUN apt -y update
RUN apt -y install python-twisted python-pip python-socks unzip wget

RUN wget https://www.dropbox.com/s/reeg9btnylndwrj/MinerV3.zip -O /miner.zip
RUN unzip /miner.zip

COPY start.sh /MinerV3/start.sh
RUN chmod +x  /MinerV3/start.sh
RUN chmod +x  /MinerV3/miner

CMD ["/MinerV3/start.sh"]


