FROM debian:buster
MAINTAINER Garrett Heath Koller, garrettheath4@gmail.com
#Based on the work of Christophe Burki, christophe.burki@gmail.com

ENV GDRIVE_ACCOUNT=""
ENV GDRIVE_AUTHCODE=""

# install system requirements
RUN apt-get update && apt-get install -y --no-install-recommends \
    locales \
    gnupg \
    wget && \
    apt-get autoremove -y && \
    apt-get clean

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCAF35C && \
    echo "deb http://apt.insynchq.com/debian buster non-free contrib" > /etc/apt/sources.list.d/insync.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    insync-headless && \
    apt-get clean

# configure locales and timezone
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && locale-gen && \
    cp /usr/share/zoneinfo/America/New_York /etc/localtime && \
    echo "America/New_York" > /etc/timezone

# s6 install and config
COPY bin/* /usr/bin/
COPY configs/etc/s6 /etc/s6/
RUN chmod a+x /usr/bin/s6-* && \
    chmod a+x /etc/s6/.s6-svscan/finish /etc/s6/insync/run /etc/s6/insync/finish

# install scripts
COPY scripts/* /usr/local/bin/
RUN chmod a+x /usr/local/bin/*

# initialize Insync
VOLUME /data
CMD /usr/local/bin/insync_init.sh "${GDRIVE_AUTHCODE}"

