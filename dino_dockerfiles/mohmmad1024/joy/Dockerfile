FROM ubuntu
LABEL maintainer="Mohammed Alsahli <mohmmad1024@gmail.com>"

RUN mkdir -p /app/joy

WORKDIR /app/joy

RUN apt-get update && apt-get install -y build-essential libssl-dev libpcap-dev libcurl4-openssl-dev git 
RUN git clone https://github.com/cisco/joy.git .
RUN ./config -l /usr/lib/x86_64-linux-gnu
RUN make
RUN cp /app/joy/bin/* /usr/local/bin/.

WORKDIR /app/joy/bin

VOLUME ["/joy/pcaps"]

CMD bash
