FROM linuxserver/webgrabplus:latest

LABEL maintainer="Òscar Casajuana <elboletaire@underave.net>"

ADD config/WebGrab++.config.xml config/providers/* /config/

ENV TZ Europe/Madrid

RUN echo $TZ > /etc/timezone

RUN chmod +x /defaults/update.sh

ENTRYPOINT [ "/defaults/update.sh" ]
