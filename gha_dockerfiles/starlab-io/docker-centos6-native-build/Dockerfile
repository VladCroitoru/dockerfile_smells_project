FROM centos:6.10
MAINTAINER Star Lab <support@starlab.io>

RUN mkdir /source

# modify CentOS repo URL following
# End-of-Life deadline
ARG DISTROVER=6.10
RUN sed -i "s/^mirrorlist.*$/baseurl=http:\/\/vault.centos.org\/${DISTROVER}\/os\/\$basearch\//g" /etc/yum.repos.d/CentOS-Base.repo

# update certificates
RUN yum -y update ca-certificates nss curl && \
    yum clean all && \
    rm -rf /var/cache/yum/* /tmp/* /var/tmp/*

# general packages and dependencies
RUN yum install --disablerepo=updates,extras -y kernel-devel bc wget \
        openssl openssl-devel python-setuptools python-virtualenv \
        dracut-network nfs-utils check unzip rpm-build rpm-devel \
        gcc perl elfutils-libelf-devel vim-common attr python-devel \
        freetype-devel sudo strace ltrace man texinfo glibc.x86_64 libgcc.x86_64 \
        glibc-devel.x86_64 glibc-static.x86_64 glibc-static.i686 automake \
        glibc.i686 glibc-devel.i686 libgcc.i686 yum-utils \
        zlib-devel sqlite-devel bzip2-devel xz-libs pigz \
        gcc-c++ zip2-devel readline-devel gdbm-devel db4-devel \
        libpcap-devel xz expat-devel && \
    yum groupinstall --disablerepo=updates,extras -y "Development Tools" && \
    yum clean all && \
    rm -rf /var/cache/yum/* /tmp/* /var/tmp/*

# remove regular git if already installed and install wandisco RPM so we can
# get a recent version of git (> v2.0)
RUN yum remove -y git && \
    rpm -ivh http://opensource.wandisco.com/centos/6/git/x86_64/wandisco-git-release-6-1.noarch.rpm && \
    yum install -y git && \
    yum clean all && \
    rm -rf /var/cache/yum/* /tmp/* /var/tmp/*

# Build and install python 2.7 and pip pinned to less than v21
RUN wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tar.xz && \
    tar xfJ Python-2.7.18.tar.xz
WORKDIR Python-2.7.18
RUN ./configure --prefix=/usr/local && make && make altinstall && \
    ln -s /usr/local/bin/python2.7 /usr/local/bin/python && \
    ln -s /usr/local/bin/python2.7 /usr/local/bin/python2
WORKDIR /
RUN rm -rf /Python-2.7.18*
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && \
    python2 ./get-pip.py && \
    python2 -m pip install --upgrade "pip < 21.0" && \
    rm ./get-pip.py

# install common packages we use in CI environments
RUN pip install numpy==1.16.0 xattr requests behave pyhamcrest matplotlib==2.2.3

# install shellcheck for sanity checking bash scripts
ARG SHELLCHECK_VER=v0.7.0
RUN wget https://github.com/koalaman/shellcheck/releases/download/${SHELLCHECK_VER}/shellcheck-${SHELLCHECK_VER}.linux.x86_64.tar.xz && \
    tar xf shellcheck-${SHELLCHECK_VER}.linux.x86_64.tar.xz && \
    install shellcheck-${SHELLCHECK_VER}/shellcheck /usr/local/bin && \
    rm -f shellcheck-${SHELLCHECK_VER}.linux.x86_64.tar.xz && \
    rm -rf shellcheck-${SHELLCHECK_VER}

# Download, build and install Python 3.6.8 and upgrade pip3
RUN wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz && \
    tar xfJ Python-3.6.8.tar.xz
WORKDIR Python-3.6.8
RUN ./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib" && \
    make && make altinstall && ln -s /usr/local/bin/python3.6 /usr/local/bin/python3
WORKDIR /
RUN rm -rf /Python-3.6.8*
RUN /usr/local/bin/python3 -m pip install --upgrade pip

# add our custom Star Lab binary helper to use sudo in the container
# and add /usr/local/bin to the path for `sudo`
ARG VER=1
ARG ZIP_FILE=add-user-to-sudoers.zip
RUN wget "https://github.com/starlab-io/add-user-to-sudoers/releases/download/${VER}/${ZIP_FILE}" && \
    unzip "${ZIP_FILE}" && \
    rm -f "${ZIP_FILE}" && \
    mkdir -p /usr/local/bin && \
    mv add_user_to_sudoers /usr/local/bin/ && \
    mv startup_script /usr/local/bin/ && \
    chmod 4755 /usr/local/bin/add_user_to_sudoers && \
    chmod +x /usr/local/bin/startup_script && \
    # Let regular users be able to use sudo
    echo $'auth       sufficient    pam_permit.so\n\
account    sufficient    pam_permit.so\n\
session    sufficient    pam_permit.so\n\
' > /etc/pam.d/sudo

# add /usr/local/bin to sudo's $PATH and don't require tty for sudo commands
RUN sed '/secure_path/ s/$/:\/usr\/local\/bin/' -i /etc/sudoers && \
    sed '/requiretty/ s/^/#/'  -i /etc/sudoers

# setup language environments
ENV LC_ALL=en_US.utf-8
ENV LANG=en_US.utf-8

VOLUME ["/source"]
WORKDIR /source
ENTRYPOINT ["/usr/local/bin/startup_script"]
CMD ["/bin/bash", "-l"]
