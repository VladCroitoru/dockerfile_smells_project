FROM centos:7

### Envrionment config
ENV HOME=/root \
    INST_SCRIPTS=/root/install

### Add all install scripts for further steps
ADD ./install/ $INST_SCRIPTS/
RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +

# Config HTTP Proxy
ARG PROXY=
RUN $INST_SCRIPTS/http_proxy.sh

# system update
RUN yum -y update && yum clean all

# Install tools
RUN $INST_SCRIPTS/tools.sh

# Set Locale
RUN rm -f /etc/rpm/macros.image-language-conf && \
    sed -i '/^override_install_langs=/d' /etc/yum.conf
RUN yum reinstall -y glibc-common && \
    yum clean all

ENV LANG="ja_JP.UTF-8" \
    LANGUAGE="ja_JP:ja" \
    LC_ALL="ja_JP.UTF-8"

