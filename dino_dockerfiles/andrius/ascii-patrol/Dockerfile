FROM alpine:edge

WORKDIR /app
RUN apk add --update --allow-untrusted --repository http://dl-4.alpinelinux.org/alpine/edge/community/ \
            curl \
            libx11 \
            libxi \
            pulseaudio \
&&  apk add --virtual .build-dependencies \
            build-base \
            git \
            libx11-dev \
            libxi-dev \
            linux-headers \
            pulseaudio-dev \
&& git clone https://github.com/msokalski/ascii-patrol.git /usr/src/ascii-patrol \
&& cd /usr/src/ascii-patrol \
&& ./build.sh \
&& cp run.sh /app \
&& cp asciipat /app \
&& cd /app \
&& apk del --purge .build-dependencies \
&& rm -rf /usr/src/ascii-patrol \
          /var/cache/apk/* \
          /tmp/* \
          /var/tmp/*

CMD ["sh", "-c", "./run.sh"]
