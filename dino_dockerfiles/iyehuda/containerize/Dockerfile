FROM docker:stable-dind

LABEL maintainer="Yehuda Chikvashvili"

ADD ./entrypoint.sh ./user-entrypoint.sh ./

# Install SSH server
RUN apk update && \
    apk add openssh-server

# Create docker group
RUN addgroup docker

ENTRYPOINT [ "/entrypoint.sh" ]

EXPOSE 22
