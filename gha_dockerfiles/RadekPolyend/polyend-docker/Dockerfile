FROM debian:9

RUN apt update
RUN apt install -y --fix-missing gawk wget git-core diffstat unzip texinfo gcc-multilib \
    build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
		xz-utils debianutils iputils-ping python3-git python3-jinja2 libegl1-mesa libsdl1.2-dev \
		pylint3 xterm locales locales-all curl bc libreadline-dev binutils-dev ctags cscope vim \
		screen apt-transport-https ca-certificates curl gnupg2 software-properties-common

RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt update
RUN apt-cache policy docker-ce
RUN apt install -y docker-ce

RUN mkdir -p /usr/local/bin
RUN curl https://storage.googleapis.com/git-repo-downloads/repo-1 > /usr/local/bin/repo
RUN chmod a+x /usr/local/bin/repo

RUN useradd -m -s /bin/bash -G root -u 1000 yocto

RUN mkdir -p /root/.docker/cli-plugins
RUN mkdir -p /home/yocto/.docker/cli-plugins

RUN wget https://github.com/docker/buildx/releases/download/v0.6.3/buildx-v0.6.3.linux-amd64

RUN cp buildx-v0.6.3.linux-amd64 /root/.docker/cli-plugins/docker-buildx
RUN mv buildx-v0.6.3.linux-amd64 /home/yocto/.docker/cli-plugins/docker-buildx

RUN chmod a+x /root/.docker/cli-plugins/docker-buildx
RUN chmod a+x /home/yocto/.docker/cli-plugins/docker-buildx

ENV LANG=en_US.UTF-8
ENV PATH=/usr/local/bin:$PATH

ENTRYPOINT ["/bin/bash"]
