FROM desktopcontainers/base-alpine

RUN apk add --no-cache easytag \
 \
 && echo 'easytag $*' >> /container/scripts/app \
 \
 && sed -i 's/# PRE-RUN PHASE/# PRE-RUN PHASE\nchmod a+rwx -R \/rips/g' /container/scripts/entrypoint.sh