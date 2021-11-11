FROM ubuntu:16.04

RUN apt-get update && apt-get install -y unzip wget curl apt-transport-https && apt-get clean

ARG CRYPTOGRAMBOT_VERSION=0.3.313
ENV CRYPTOGRAMBOT_VERSION ${CRYPTOGRAMBOT_VERSION}

RUN mkdir -p /cryptogrambot
WORKDIR /cryptogrambot

RUN wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get update && apt-get install -y dotnet-sdk-2.1 && apt-get clean

RUN wget https://github.com/mehtadone/CryptoGramBot/releases/download/CryptoGramBot-v$CRYPTOGRAMBOT_VERSION/CryptoGramBot-v$CRYPTOGRAMBOT_VERSION.zip
RUN unzip CryptoGramBot-v$CRYPTOGRAMBOT_VERSION.zip

VOLUME /cryptogrambot/

CMD dotnet CryptoGramBot.dll

EXPOSE 5002
