FROM       postgres:9.6-alpine
MAINTAINER Carlos Avila "cavila@mandelbrew.com"

# Prep environment
ENV        MANTRA_PRE_FETCH='' \
           MANTRA_POST_FETCH='' \
           MANTRA_FETCH_URL='' \
           MANTRA_SPEC='' \
           MANTRA_CMD='' \
           MANTRA_CMD_ARGS=''

# Operating System
RUN        apk update \
           && apk add --no-cache \
               curl

# Application
WORKDIR	   /root

ADD        https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra /usr/local/bin/mantra
RUN        chmod +x /usr/local/bin/mantra

ADD        scripts/docker-cmd.sh docker-cmd.sh
RUN        chmod +x docker-cmd.sh

CMD        ["./docker-cmd.sh"]