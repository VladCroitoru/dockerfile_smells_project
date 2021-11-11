FROM centos:centos7

MAINTAINER Diego Castro <diego.castro@getupcloud.com>

ENV HOME=/data

RUN INSTALL_PKGS="nodejs npm mariadb rh-postgresql94 rh-mongodb26-mongodb telnet" && \
    yum install -y epel-release centos-release-scl && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    yum clean all -y
    
RUN npm install -g azure-cli

RUN mkdir -p ${HOME} && chmod 777 ${HOME}

ADD root /

ENV CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts \
    ENABLED_COLLECTIONS="rh-postgresql94 rh-mongodb26"

ENV BASH_ENV=${CONTAINER_SCRIPTS_PATH}/scl_enable \
    ENV=${CONTAINER_SCRIPTS_PATH}/scl_enable \
    PROMPT_COMMAND=". ${CONTAINER_SCRIPTS_PATH}/scl_enable"

VOLUME ${HOME}

USER 1000

ENTRYPOINT ["container-entrypoint"]
CMD ["run"]
