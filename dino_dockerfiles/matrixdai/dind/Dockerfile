FROM debian:jessie

LABEL author="Matrix Dai <sexiszero@gmail.com>"

ENV DOCKER_BUCKET="get.docker.com" \
    DOCKER_VERSION="1.13.0" \
    DOCKER_SHA256="fc194bb95640b1396283e5b23b5ff9d1b69a5e418b5b3d774f303a7642162ad6" \
    DIND_COMMIT="3b5fac462d21ca164b3778647420016315289034" \
    TERM=xterm

# Install packages
RUN set -x && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    curl wget vim zip man telnet net-tools python git subversion dos2unix cifs-utils screen xfsprogs iptables nload openldap-utils && \
    apt-get clean all && \
    curl -s https://bootstrap.pypa.io/get-pip.py | python && \
    pip install awscli && \
    curl -Lo git-lfs.deb https://packagecloud.io/github/git-lfs/packages/debian/jessie/git-lfs_2.0.1_amd64.deb/download && \
    dpkg -i git-lfs.deb && \
    rm -rf git-lfs.deb

# Setup docker
RUN set -x && \
    curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o docker.tgz && \
    echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - && \
    tar -xzvf docker.tgz && \
    mv docker/* /usr/local/bin/ && \
    rmdir docker && \
    rm docker.tgz && \
    curl -L "https://github.com/docker/compose/releases/download/1.10.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose && \
    addgroup --system dockremap && \
    adduser --system --group dockremap && \
    echo 'dockremap:165536:65536' >> /etc/subuid && \
    echo 'dockremap:165536:65536' >> /etc/subgid && \
    curl "https://raw.githubusercontent.com/docker/docker/${DIND_COMMIT}/hack/dind" -o /usr/local/bin/dind && \
    chmod +x /usr/local/bin/dind

# Enable vim syntax color
RUN sed -i "s/\"syntax on/syntax on/g" /etc/vim/vimrc

# Custom PS1
# RUN echo 'export PS1="\[$(tput bold)\]\[$(tput setaf 1)\][\[$(tput setaf 3)\]D\[$(tput setaf 5)\]o\[$(tput setaf 6)\]c\[$(tput setaf 4)\]k\[$(tput setaf 2)\]e\[$(tput setaf 3)\]r\[$(tput setaf 2)\] \w\[$(tput setaf 1)\]]\[$(tput setaf 7)\]\$ \[$(tput sgr0)\]"' >> /etc/bash.bashrc
RUN sed -i 's/^PS1=.*$/PS1="\\[$(tput bold)\\]\\[$(tput setaf 1)\\][\\[$(tput setaf 3)\\]D\\[$(tput setaf 5)\\]o\\[$(tput setaf 6)\\]c\\[$(tput setaf 4)\\]k\\[$(tput setaf 2)\\]e\\[$(tput setaf 3)\\]r\\[$(tput setaf 2)\\] \\w\\[$(tput setaf 1)\\]]\\[$(tput setaf 7)\\]\\$ \\[$(tput sgr0)\\]"/g' /etc/bash.bashrc


COPY entrypoint.sh /usr/local/bin/

VOLUME /var/lib/docker
EXPOSE 2375

WORKDIR /root
ENTRYPOINT ["entrypoint.sh"]
