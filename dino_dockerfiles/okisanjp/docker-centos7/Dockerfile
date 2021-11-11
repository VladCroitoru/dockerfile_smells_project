FROM centos:7
LABEL maintainer "okisanjp <okisan.jp@gmail.com>"

# yum update
RUN yum -y update && yum clean all

# localize to japanese
ENV LANG="ja_JP.UTF-8" \
    LC_ALL="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja"
		
RUN yum -y reinstall glibc-common && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
    unlink /etc/localtime && \
    ln -s /usr/share/zoneinfo/Japan /etc/localtime

# install some tools
RUN yum -y --setopt=tsflags='' install \
    man-pages \
    man-pages-ja \
    vim-enhanced
