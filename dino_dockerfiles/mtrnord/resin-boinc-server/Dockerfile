FROM resin/armv7hf-debian-qemu

MAINTAINER MTRNord <info@nordgedanken.de>

RUN [ "cross-build-start" ]
ENV DOCKER_HOST unix:///var/run/rce.sock

#install packages
RUN apt-get update && apt-get install -y \
        git \
        apt-transport-https \
        ca-certificates \
        make \
        build-essential \
        wget

# Install resin.io's rce (docker)
COPY ./rce /usr/bin/rce
RUN chmod +x /usr/bin/rce
RUN ln -s /usr/bin/rce /usr/bin/docker
RUN chmod +x /usr/bin/docker
RUN rm -rf /var/run/rce.pid

RUN apt-get update && apt-get install -y apt-transport-https && echo "deb https://packagecloud.io/Hypriot/Schatzkiste/debian/ jessie main" | tee /etc/apt/sources.list.d/hypriot.list && apt-get update && apt-get install -y --force-yes docker-compose

#configure server
RUN git clone --recursive https://github.com/MTRNord/boinc-server-docker.git && cd boinc-server-docker && git checkout rpi && cd ..
RUN echo "127.0.0.1 http://ProjectStreet.dynu.com" >> /etc/hosts

# Define additional metadata for our image.
VOLUME /var/lib/rce
RUN ln -s /var/lib/rce /var/lib/docker

COPY . /app

RUN [ "cross-build-end" ]

CMD ["/bin/bash", "/app/start"]
