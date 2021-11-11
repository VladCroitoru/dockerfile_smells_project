FROM akhilnairamey/sparklyr:R_3.4.1-sparklyr_0.6.1-dplyr_0.7.2

# Install python-dev, pip and docker-machine
RUN apt-get update && apt-get install python-setuptools python-dev build-essential curl -y \
  && sudo easy_install pip \
  && curl -L \
      https://github.com/docker/machine/releases/download/v0.12.2/docker-machine-`uname -s`-`uname -m` \
    > /tmp/docker-machine \
  && chmod +x /tmp/docker-machine \
  && cp /tmp/docker-machine /usr/local/bin/docker-machine

# Create cipher working directory
RUN mkdir /root/cipher
WORKDIR /root/cipher
COPY requirements.txt /root/cipher

# Install cipher pip requirements
RUN pip install -r requirements.txt
RUN pip install awscli

# Install R libraries 
RUN R -e "devtools::install_github('AkhilNairAmey/crassy')"
RUN R -e "devtools::install_github('AkhilNairAmey/CQLConnect@v2.1.0')"
