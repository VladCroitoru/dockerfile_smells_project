FROM ubuntu:14.04

MAINTAINER Adrien Folie, folie.adrien@gmail.com

# Install dependencies
RUN apt-get update -qq && \
    apt-get install -qy \
    wget \
    python \
    python-cheetah

# Set SickRage version
ENV VERSION 4.0.9
ENV APP /home/.sickrage

# Install SickRage
RUN wget https://github.com/SiCKRAGETV/SickRage/archive/v$VERSION.tar.gz && \
    tar -xzvf v$VERSION.tar.gz && \
    rm v$VERSION.tar.gz && \
    mv SickRage-$VERSION $APP && \
    cd $APP && \
    cp -a autoProcessTV/autoProcessTV.cfg.sample autoProcessTV/autoProcessTV.cfg

VOLUME /config
VOLUME /data

COPY run.sh /home/run.sh
RUN chmod +x /home/run.sh

WORKDIR /home
EXPOSE 8081

# Start SickRage
ENTRYPOINT ["./run.sh"]
