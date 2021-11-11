
MAINTAINER Grigorii Sokolik <g.sokol99@g-sokol.info>

VOLUME ["/app", "/ssh"]

WORKDIR "/app"

COPY install.sh /install.sh

RUN apk update \
  && apk add ca-certificates openssh-client \
    openssl git mercurial subversion bzr glide \
  && update-ca-certificates \
  && echo -e "StrictHostKeyChecking no" >> /etc/ssh/ssh_config \
  && chmod 700 /install.sh

ENTRYPOINT ["/install.sh"]
