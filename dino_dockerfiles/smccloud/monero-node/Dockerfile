FROM ubuntu:18.04
MAINTAINER Shaun McCloud<git@smccloud.com>
LABEL version="v0.13.0.4"

# Copy shell scripts
ADD run.sh /

# Setup the image
RUN apt-get update
RUN apt-get install -y wget bzip2
RUN wget -O /monero-linux-x64-v0.13.0.4.tar.bz2 https://github.com/monero-project/monero/releases/download/v0.13.0.4/monero-linux-x64-v0.13.0.4.tar.bz2
RUN tar xvf /monero-linux-x64-v0.13.0.4.tar.bz2
RUN rm -f /monero-linux-x64-v0.13.0.4.tar.bz2
RUN mv /monero-v0.13.0.4 /monero
RUN mkdir -p /blockchain

# Stop the container
STOPSIGNAL SIGTERM

# Expose the two ports needed for the Monero daemon
EXPOSE 18080 18081

# Expose a volume for blockchain storage
VOLUME ["/blockchain"]

#CMD ["/bin/bash", "/run.sh"]
ENTRYPOINT ["/monero/monerod"," --data-dir=/blockchain --block-sync-size=20 --rpc-bind-ip=0.0.0.0 --restricted-rpc --confirm-external-bind --detach --log-file=/blockchain/bitmonero.log"]
