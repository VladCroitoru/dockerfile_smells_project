FROM alpine:3.10

ENV WORKSPACE /home/devuser

# Installing build tools
RUN apk --update add \
    bash \
    tar \
    git \
    nodejs \
    npm \
    jq \
    curl


RUN addgroup staff
RUN adduser -D -g "" -G staff -s /bin/bash devuser
RUN echo "devuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN touch ${WORKSPACE}/.bashrc
RUN chown -R devuser:staff ${WORKSPACE}

# Installing the JS toolchain
RUN npm install -g @angular/cli

USER devuser
WORKDIR ${WORKSPACE}
