FROM nodered/node-red-docker:slim

ENV USERNAME=app
ENV PASSWORD=ppa
ENV SSH_PORT=2022
ENV RED_PORT=1880

USER root

RUN apk --no-cache upgrade \
 && apk --no-cache add \
    cmake libuv-dev build-base \
    sudo bash wget curl openssh git \
    python \
    ffmpeg

RUN adduser -D -G root -s /bin/bash -h /home/$USERNAME $USERNAME \
 && echo "$USERNAME:$PASSWORD" | chpasswd \
 && export USERNAME=$USERNAME

# Grant privileges
RUN chgrp -R 0     /var /etc /home/$USERNAME \
 && chmod -R g+rwX /var /etc /home/$USERNAME \
 && sed -i 's/#\s%wheel/%root/' /etc/sudoers \
 && chmod 664 /etc/passwd /etc/group

# Install dumb-init (avoid PID 1 issues). https://github.com/Yelp/dumb-init
RUN curl -Lo /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 \
 && chmod +x /usr/local/bin/dumb-init

# Prepare SSH service
RUN echo "Port $SSH_PORT" >> /etc/ssh/sshd_config \
 && mkdir -p /var/empty && chmod 700 /var/empty \
 && export SSH_PORT=$SSH_PORT

USER node-red
EXPOSE $RED_PORT
VOLUME /var/log/pods
VOLUME /data

ADD entrypoint.sh /
ENTRYPOINT  ["dumb-init","/entrypoint.sh"]
