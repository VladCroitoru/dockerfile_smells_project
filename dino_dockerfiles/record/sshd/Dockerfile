FROM alpine:3.6

RUN apk add --no-cache \
        bash \
        bash-completion \
        openssh \
        sudo \
    && true

RUN adduser \
        -D \
        -s /bin/bash \
        ubuntu && \
    echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/90-ubuntu && \
    (echo "ubuntu:ubuntu" | chpasswd) && \
    ssh-keygen -A

EXPOSE 22

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
