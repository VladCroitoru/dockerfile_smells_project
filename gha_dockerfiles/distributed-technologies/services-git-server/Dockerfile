FROM alpine:3.14

WORKDIR /git-server/

RUN apk add --no-cache openssh git

COPY sshd_config /etc/ssh/sshd_config

COPY start.sh /git-server/

RUN git config --global init.defaultBranch main

RUN mkdir /git-server/keys \
  && adduser -D -s /usr/bin/git-shell git \
  && mkdir /home/git/.ssh \
  && echo git:* | chpasswd -e \
  && chown git:git /home/git/.ssh

EXPOSE 22

CMD [ "sh", "start.sh" ] 
