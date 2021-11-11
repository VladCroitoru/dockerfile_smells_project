FROM docker.io/kalilinux/kali-rolling:latest
RUN apt -y update && apt -y dist-upgrade && \ 
    apt -y install \
    util-linux \
    git \
    bash \
    vim \
    sslscan 
RUN echo "alias l='ls -lrth'" >> /root/.bashrc && \
    echo "alias c='clear'" >> /root/.bashrc && \
    echo "alias ll='ls -lth'" >> /root/.bashrc && \
    echo "alias la='ls -larth'" >> /root/.bashrc
ENTRYPOINT ["/bin/bash"]
