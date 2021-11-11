FROM debian:jessie
MAINTAINER Andreas Krüger
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq && apt-get install --no-install-recommends --no-install-suggests -yqq build-essential openssl libxml2-dev libncurses5-dev uuid-dev sqlite3 libsqlite3-dev pkg-config curl libjansson-dev libgtk2.0-dev && rm -rf /var/lib/apt/lists/*

# Download and decompress latest asterisk version
RUN curl -s http://downloads.asterisk.org/pub/telephony/certified-asterisk/certified-asterisk-13.1-current.tar.gz | tar xz

# Asterisk compilation & installation
WORKDIR /certified-asterisk-13.1-cert2
RUN ./configure;
RUN make menuselect.makeopts
RUN sed -i "s/BUILD_NATIVE//" menuselect.makeopts
RUN make; make install; make samples

RUN mkdir -p /etc/asterisk

# ADD modules.conf /etc/asterisk/
COPY iax.conf /etc/asterisk/
COPY extensions.conf /etc/asterisk/

CMD ["/usr/sbin/asterisk", "-f"]
