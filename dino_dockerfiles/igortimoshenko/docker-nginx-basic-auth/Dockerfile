FROM nginx

ENV DEBIAN_FRONTEND=noninteractive \
    TERM=xterm

RUN apt-get update -y \
    && apt-get install -y \
        apache2-utils \
    && rm -rf /var/lib/apt/lists/*

COPY basic-auth.conf entrypoint.sh /
RUN chmod 0755 /entrypoint.sh

CMD /entrypoint.sh
