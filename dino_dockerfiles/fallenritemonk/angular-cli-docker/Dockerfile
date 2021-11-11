FROM debian:8.6

RUN apt-get update && apt-get install -y curl apt-transport-https ca-certificates python make gcc
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo 'deb https://apt.dockerproject.org/repo debian-jessie main' >> /etc/apt/sources.list.d/docker.list
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get update && apt-get install -y docker-engine nodejs build-essential
RUN npm install -g @angular/cli@1.2.0
RUN systemctl enable docker
