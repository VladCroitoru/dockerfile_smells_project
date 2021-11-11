FROM mwaeckerlin/base

ENV TIMEOUT "600"
ENV BOAR_USER "boar"
ENV BOAR_HOST "boar"
ENV BOAR_PORT "22"
ENV BOAR_REPO "boar+ssh://BOAR_USER@BOAR_HOST/boar"
ENV BOAR_SOURCE "https://bitbucket.org/mats_ekberg/boar/downloads/boar.16-Nov-2012.tar.gz"
ENV LANG "en_US.UTF-8"
ENV SSH_PUBKEY ""
ENV SSH_PRIVKEY ""
ENV OPTIONS "-q"

WORKDIR /opt
RUN $PKG_INSTALL openssh-client inotify-tools python wget \
 && wget -O- ${BOAR_SOURCE} | tar xz \
 && $PKG_REMOVE wget \
 && mkdir /data \
 && chown ${RUN_USER}:${RUN_GROUP} /data
ADD boar /usr/local/bin/boar
WORKDIR /data
USER $RUN_USER

VOLUME /data
