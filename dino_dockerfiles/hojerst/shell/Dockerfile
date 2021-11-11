FROM quay.io/skopeo/stable:v1.2.0@sha256:1143edac7c251ff3cd756d94bfd4d2e83a1353dd05cf4dcf73e2f5100b391d44 AS skopeo
FROM ubuntu:20.04@sha256:c95a8e48bf88e9849f3e0f723d9f49fa12c5a00cfc6e60d2bc99d87555295e4c AS downloads

WORKDIR /work

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
        curl=7.68.0-1ubuntu2.4 \
        ca-certificates=20201027ubuntu0.20.04.1
RUN curl -L -o kubectl https://storage.googleapis.com/kubernetes-release/release/v1.20.0/bin/linux/amd64/kubectl
RUN chmod 0755 kubectl

FROM ubuntu:20.04@sha256:c95a8e48bf88e9849f3e0f723d9f49fa12c5a00cfc6e60d2bc99d87555295e4c

# install additional software
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install --no-install-recommends -y \
        man-db=2.9.1-1 \
        vim=2:8.1.2269-1ubuntu5 \
        git=1:2.25.1-1ubuntu3 \
        zsh=5.8-3ubuntu1 \
        curl=7.68.0-1ubuntu2.4 \
        dnsutils=1:9.16.1-0ubuntu2.4 \
        iproute2=5.5.0-1ubuntu1 \
        iputils-ping=3:20190709-3 \
        telnet=0.17-41.2build1 \
        httpie=1.0.3-2 \
        fzf=0.20.0-1 \
        ripgrep=11.0.2-1build1 \
        swaks=20190914.0-1 \
        netcat=1.206-1ubuntu1 \
        yadm=2.3.0-2 \
        locales=2.31-0ubuntu9.1 \
        openssh-client=1:8.2p1-4ubuntu0.1 \
        libgpgme11=1.13.1-7ubuntu2 \
        libdevmapper1.02.1=2:1.02.167-1ubuntu1 \
        direnv=2.21.2-1 \
        ca-certificates=20201027ubuntu0.20.04.1 && \
    yadm clone https://gitlab.com/hojerst/dotfiles.git -f --bootstrap && \
    /bin/zsh -c "SSH_AUTH_SOCK=/dev/null source /root/.zshrc" && \
    locale-gen en_GB.UTF-8 && \
    ln -sf libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/libdevmapper.so.1.02 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=downloads /work/kubectl /usr/local/bin/
COPY --from=skopeo /etc/containers /etc
COPY --from=skopeo /usr/bin/skopeo /usr/local/bin

ENV SHELL /bin/zsh
WORKDIR /root

CMD [ "/bin/zsh", "--login" ]
