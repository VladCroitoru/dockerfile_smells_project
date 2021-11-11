FROM ubuntu:trusty

VOLUME ["/server/config"]

EXPOSE 27888

WORKDIR /server
CMD ["/run.sh"]

ENV K_FILE kaillerasrv-0.86-linux.tgz
ENV K_URL http://kaillera.com/files/kaillerasrv-0.86-linux.tgz
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y -q install curl lib32z1 lib32ncurses5 lib32bz2-1.0 && \
    curl -sLo /server/${K_FILE} ${K_URL} && \
    tar zxvf /server/${K_FILE} --strip=1 -C /server && \
    rm -f /server/${K_FILE} && \
    mv /server/kaillerasrv.conf /server/config/kaillerasrv.conf && \
    ln -sf /server/kaillerasrv.conf /server/config/kaillerasrv.conf

ADD rootfs /

ARG VERSION
ARG BUILD_DATE
ARG VCS_REF

LABEL org.label-schema.version=$VERSION
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.vcs-ref=$VCS_REF
LABEL org.label-schema.vcs-url="https://github.com/alpharde/docker-kaillera.git"
LABEL org.label-schema.name="Kaillera Server"
LABEL org.label-schema.schema-version="0.86"
