FROM bitwalker/alpine-erlang:20.1
RUN echo "http://dl-2.alpinelinux.org/alpine/v3.6/main" >> /etc/apk/repositories && \
    echo "http://dl-3.alpinelinux.org/alpine/v3.6/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.6/main" >> /etc/apk/repositories && \
    echo "http://dl-5.alpinelinux.org/alpine/v3.6/main" >> /etc/apk/repositories && \
    apk update && \
    apk --no-cache --update add libgcc libstdc++ bash && \
    rm -rf /var/cache/apk/*
