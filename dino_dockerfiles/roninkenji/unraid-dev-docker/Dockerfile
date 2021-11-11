FROM roninkenji/slackware-full
MAINTAINER roninkenji

RUN useradd -ms /bin/bash -u 1000 -g 100 devuser
COPY devuser.sudo /etc/sudoers.d/devuser
ENTRYPOINT ["/bin/sh", "-c", "while true; do sleep 86400; done;"]

USER devuser
WORKDIR /home/devuser

