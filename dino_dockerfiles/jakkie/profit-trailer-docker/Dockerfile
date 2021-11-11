
FROM ubuntu:16.04

RUN apt-get update && apt-get install -y unzip curl openjdk-8-jdk
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh && bash nodesource_setup.sh
RUN apt-get install -y nodejs && apt-get clean
RUN npm install pm2@latest -g

ARG PT_VERSION=2.2.12
ENV PT_VERSION ${PT_VERSION}

RUN mkdir -p /app/

RUN curl https://github.com/taniman/profit-trailer/releases/download/$PT_VERSION/ProfitTrailer-$PT_VERSION.zip -L -o /app/profittrailer.zip
RUN unzip /app/profittrailer.zip -d /app/ && mv /app/ProfitTrailer-$PT_VERSION /app/ProfitTrailer

WORKDIR /app/ProfitTrailer
RUN chmod +x ProfitTrailer.jar

VOLUME /app/ProfitTrailer

CMD pm2 start pm2-ProfitTrailer.json && pm2 log 0

EXPOSE 8081