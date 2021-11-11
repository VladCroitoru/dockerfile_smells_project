FROM debian:8

RUN apt-get update && apt-get install -y wget
RUN mkdir /src /app
RUN wget https://raw.githubusercontent.com/schorsch3000/localn/master/src/localn.sh -O /app/localn
RUN chmod +x /app/localn
COPY app/* app/
WORKDIR /app
ENV PATH=/app/.localn/bin/:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
RUN /app/localn stable
RUN npm i
RUN npm i -g gulp

ENTRYPOINT gulp