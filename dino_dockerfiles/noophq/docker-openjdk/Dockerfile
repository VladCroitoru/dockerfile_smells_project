FROM openjdk:8-jdk-alpine

# Install docker
RUN apk update --no-cache && \
    apk add docker py-pip

# Install docker-compose
RUN pip install docker-compose

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
# Install docker at boot
#RUN rc-update add docker boot
