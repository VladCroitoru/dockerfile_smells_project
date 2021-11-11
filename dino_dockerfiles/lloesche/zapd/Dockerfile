FROM debian:jessie
EXPOSE 18301

COPY zapwireless /zapwireless/
COPY run.sh /

RUN apt-get update && \
    apt-get -y install build-essential

RUN cd zapwireless && \
    make && \
    make install && \
    cd / && \
    rm -rf /zapwireless

RUN apt-get -yf remove --auto-remove build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /

CMD ["/run.sh"]
