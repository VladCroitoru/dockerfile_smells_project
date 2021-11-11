FROM centos:7
MAINTAINER Thiago Figueiro thiago.figueiro@bt.com

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
    && yum update -y \
    && yum install -y \
    make \
    pandoc \
    perl-Tk \
    perl-Digest-MD5 \
    python-pip \
    wget \
    && localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-archive \
    && mv -f /usr/lib/locale/locale-archive /usr/lib/locale/locale-archive.tmpl \
    && build-locale-archive \
    && find /usr/share/i18n/locales/ -type f | grep -v /en | xargs rm \
    && yum clean all \
    && rpmdb --rebuilddb

ADD texlive.profile /tmp/
RUN mkdir /tmp/texlive \
    && cd /tmp/texlive \
    && curl -Lo install-tl-unx.tar.gz http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
    && tar zxvf install-tl-unx.tar.gz --strip-components=1 \
    && ./install-tl -profile /tmp/texlive.profile -repository http://mirror.ctan.org/systems/texlive/tlnet/ \
    && rm -rf /tmp/texlive

ENV PATH=/usr/local/texlive/2016/bin/x86_64-linux:$PATH
RUN pip install \
    pypandoc \
    pyaml \
    texttable\
    Sphinx

