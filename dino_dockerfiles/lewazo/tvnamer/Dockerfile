FROM alpine:3.7
LABEL maintainer="lewazo"

RUN apk add --no-cache py-setuptools shadow bash su-exec
RUN ./usr/bin/easy_install-2.7 tvnamer

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod o+x /usr/local/bin/entrypoint.sh

VOLUME ["/config", "/tv"]

WORKDIR /tv

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
