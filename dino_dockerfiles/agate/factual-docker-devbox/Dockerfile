FROM factual/docker-cdh5-devbox

MAINTAINER agate<agate.hao@gmail.com>

RUN apt-get update
RUN apt-get install -y byobu vim-nox curl wget mosh
RUN apt-get install -y libsqlite3-dev
RUN apt-get install -y apt-utils
RUN apt-get -y upgrade

RUN apt-get install -y apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee /etc/apt/sources.list.d/docker.list
RUN apt-get update
RUN apt-get install -y docker-engine
RUN curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

RUN apt-get install -y postgresql-client
# For pyenv
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
                       libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
