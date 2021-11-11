#FROM alfg/ffmpeg:latest
FROM debian:latest

#WORKDIR /app
COPY ./target/release/benson /app/benson
WORKDIR /app
#RUN echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null

# RUN apt-get update -y
# RUN apt-get install software-properties-common -y
# RUN add-apt-repository universe
RUN apt-get clean -y
RUN apt-get update -y
#RUN apt-get install -y openssl-dev
RUN apt-get install -y ffmpeg
# RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
# RUN chmod a+rx /usr/local/bin/youtube-dl

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
COPY ./config.json ./config.json
RUN cp /app/config.json /config.json

ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]
