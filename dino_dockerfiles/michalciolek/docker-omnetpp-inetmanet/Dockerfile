FROM ryankurte/docker-omnetpp
MAINTAINER Michał Ciołek <michal.ciolek@wat.edu.pl>
LABEL Description="Docker image for OMNeT++ Network Simulator with custom inetmanet-3.x"

# Download inetmanet-3.x

RUN cd /usr/omnetpp/omnetpp-5.2/samples && \
    git clone --recursive https://github.com/michalciolek/inetmanet-3.x.git && \
    cd inetmanet-3.x && \
    git reset --hard ec78ef9a4c0d6af63faabaf17dc6ecfdba42770e && \
    rm -rf .git showcases/.git tutorials/.git
