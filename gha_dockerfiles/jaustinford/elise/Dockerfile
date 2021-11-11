FROM centos:8
LABEL maintainer="Austin Ford <j.austin.ford@gmail.com>"

RUN \
    yum update -y && \
    yum install -y \
        epel-release

RUN \
    yum install -y \
        tree \
        vim \
        curl \
        wget \
        htop \
        bmon \
        git \
        bc \
        nmap \
        jq \
        dos2unix \
        net-tools \
        diffutils \
        bind-utils \
        httpd-tools \
        openvpn

# ansible
RUN \
    yum install -y \
        ansible \
        python3

RUN \
    pip3 install --upgrade pip && \
    pip3 install \
        requests

RUN \
    rm -f /etc/ansible/ansible.cfg && \
    ln -s /root/ansible/ansible.cfg /etc/ansible/ansible.cfg

# youtube-dl
RUN \
    yum install -y youtube-dl && \
    dnf install -y dnf-plugins-core dnf-utils && \
    yum-config-manager -y --set-enabled powertools && \
    yum-config-manager -y --add-repo=https://negativo17.org/repos/epel-multimedia.repo && \
    dnf install -y ffmpeg

# source local profile
RUN ln -s /root/.bash_profile /etc/profile.d/elise_profile.sh

CMD ["/bin/bash"]
