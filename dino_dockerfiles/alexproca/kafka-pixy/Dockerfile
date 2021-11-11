FROM debian:jessie
MAINTAINER Alex Proca <alex.proca@gmail.com>

RUN apt-get update && apt-get install -y curl
RUN curl -L https://github.com/mailgun/kafka-pixy/releases/download/v0.11.0/kafka-pixy-v0.11.0-1-ge927f15-linux-amd64.tar.gz | tar xz
RUN ln -s /kafka-pixy-v0.11.0-1-ge927f15-linux-amd64/kafka-pixy /usr/bin/kafka-pixy

CMD ["kafka-pixy"]
