FROM debian:latest

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    libssl-dev \
    git
RUN git clone https://github.com/wg/wrk.git
WORKDIR ./wrk
RUN make
RUN cp wrk /usr/local/bin
