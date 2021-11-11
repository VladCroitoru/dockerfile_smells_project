#
# Dockerfile for SRBMiner-Multi, https://github.com/hellcatz/luckpool
# see run.sh
#
FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade && apt-get -y install screen wget xz-utils && \
    cd /opt && wget https://github.com/doktor83/SRBMiner-Multi/releases/download/0.8.1/SRBMiner-Multi-0-8-1-Linux.tar.xz && \
	tar xf SRBMiner-Multi-0-8-1-Linux.tar.xz && rm -rf /opt/SRBMiner-Multi-0-8-1-Linux.tar.xz && \
	apt-get -y purge xz-utils && apt-get -y autoremove --purge && apt-get -y clean && apt-get -y autoclean; rm -rf /var/lib/apt-get/lists/*
COPY entrypoint /opt/SRBMiner-Multi-0-8-1/
RUN chmod +x /opt/SRBMiner-Multi-0-8-1/entrypoint
# it needs a workdir spec in order to see the 'verus-solver' binary right next to it
WORKDIR "/opt/SRBMiner-Multi-0-8-1"
ENTRYPOINT "./entrypoint"
# EOF
