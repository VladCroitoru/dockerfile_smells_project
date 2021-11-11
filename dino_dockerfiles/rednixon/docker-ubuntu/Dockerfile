FROM ubuntu:18.04
MAINTAINER Red Nixon "info@rednixon.io"

RUN apt-get update \
    && apt-get install -q -y \
    apt-transport-https \
    lsb-release \
    wget \
    apt-utils \
    curl \
    nano \
    zip \
    unzip \
    python3-pip \
    git \
    ca-certificates \
	vim \
	apache2 

# Add Scripts
ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

EXPOSE 80

CMD ["/start.sh"]
