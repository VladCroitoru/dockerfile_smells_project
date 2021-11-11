FROM ghcr.io/mback2k/docker-debian/stretch:latest as build

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential autoconf automake libtool swig \
        tcl8.5-dev libssl1.0-dev libltdl-dev && \
    apt-get clean

RUN mkdir -p /app
WORKDIR /app

ADD . /app

RUN ./autogen.sh
RUN ./configure --prefix=/usr/local --with-tcl=/usr/lib/tcl8.5

RUN make
RUN make install


FROM ghcr.io/mback2k/docker-debian/stretch:latest

COPY --from=build /usr/local/bin/ /usr/local/bin/
COPY --from=build /usr/local/lib/ /usr/local/lib/
COPY --from=build /usr/local/share/ /usr/local/share/

RUN adduser --disabled-password --disabled-login --system --group \
        --uid 6667 --home /data sbnc

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tcl8.5 libssl1.0.2 libltdl7 && \
    apt-get clean

USER sbnc
EXPOSE 6667

VOLUME /data
WORKDIR /data

CMD ["/usr/local/bin/sbnc", "--foreground", "--config", "/data"]
