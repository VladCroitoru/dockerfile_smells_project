FROM alpine:latest
RUN apk update --no-cache && apk upgrade --no-cache && \
    apk add --no-cache \
    curl \ 
    git \
    util-linux \
    bash && \
    echo "alias l='ls -lrth'" >> /root/.bashrc && \
    echo "alias c='clear'" >> /root/.bashrc && \
    echo "alias ll='ls -lth'" >> /root/.bashrc && \
    echo "alias la='ls -larth'" >> /root/.bashrc
ENTRYPOINT ["/bin/bash"]

