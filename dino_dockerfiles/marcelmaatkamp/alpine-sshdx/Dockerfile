FROM library/docker:dind
MAINTAINER Daniel Guerra <daniel.guerra69@gmail.com>

RUN apk add --update openssh util-linux dbus ttf-freefont xauth xf86-input-keyboard sudo\
    && rm  -rf /tmp/* /var/cache/apk/*
RUN \
   addgroup docker \
&& addgroup alpine \
&& adduser  -G alpine -G docker -s /bin/sh -D alpine \
&& echo "alpine:alpine" | /usr/sbin/chpasswd \
&& echo "alpine    ALL=(ALL) ALL" >> /etc/sudoers

ADD docker-entrypoint.sh /usr/sbin
ENTRYPOINT ["/usr/sbin/docker-entrypoint.sh"]
CMD ["/usr/sbin/sshd","-D"]
