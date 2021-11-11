FROM ubuntu AS build
LABEL maintainer="Mfuon Leonard" MAINTAINER="Mfuon Leonard <mfolee@gmail.com>"
LABEL application="hamingBot"
ENV TERM=xterm-256color

RUN apt update -y
RUN apt install -y build-essential wget unzip git
RUN apt clean
RUN git clone https://github.com/Mfuon2/haming_bot.git
RUN cd haming_bot 
RUN pwd
RUN ls -la
RUN sleep 5
RUN chmod +x /haming_bot/entrypoint.sh
RUN /haming_bot/entrypoint.sh


