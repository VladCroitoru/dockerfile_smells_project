FROM leifg/elixir:1.5.3
LABEL maintainer="Leif Gensert <leif@leif.io>"

RUN apk add --no-cache bash busybox-extras

ADD debug.sh /usr/local/bin/

CMD ["/usr/local/bin/debug.sh"]
