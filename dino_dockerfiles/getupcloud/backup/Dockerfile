FROM openshift/origin

MAINTAINER Mateus Caruccio <mateus.caruccio@getupcloud.com>

ENV HOME=/usr/src/app \
    PATH=/usr/src/app:$PATH \
    KUBECONFIG=/usr/src/app/.kubeconfig \
    CONTAINER_SCRIPTS_PATH=/usr/share/container-scripts

ADD requirements.txt /usr/src/app/

RUN mkdir -p ${HOME} && \
    chmod 777 ${HOME} && \
    yum install -y --setopt=tsflags=nodocs epel-release && \
    INSTALL_PKGS="gcc python34-pip python34-devel openssl-devel pv" && \
    yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \
    yum clean all -y && \
    pip3 install --no-cache-dir -r /usr/src/app/requirements.txt && \
    chown 1001 -R ${HOME}

ADD root /

USER 1001

ENTRYPOINT ["container-entrypoint"]

WORKDIR $HOME

CMD ["run"]
