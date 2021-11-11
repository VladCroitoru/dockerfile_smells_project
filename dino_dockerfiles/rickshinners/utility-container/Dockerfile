FROM alpine:3.7
LABEL maintainer="rickshinners@gmail.com"

RUN apk update && \
    apk add \
        bash \
        vim \
        htop \
        ncurses \
    && rm -rf /var/cache/apk/*

COPY root /root

CMD ["/bin/bash"]