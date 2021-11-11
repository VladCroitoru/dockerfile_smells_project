FROM openshift/origin:latest

LABEL maintainer="wouter.vandenheede@axians.com"

ENV BIN_DIR=/opt/pruner \
    HOME=/etc/pruner \
    KUBECONFIG=/etc/pruner/.kubeconfig \
    WRITE_KUBECONFIG=1

RUN mkdir -p ${HOME} ${BIN_DIR} && chmod 777 ${HOME} && chmod 555 ${BIN_DIR}

COPY . ${BIN_DIR}

WORKDIR ${BIN_DIR}

VOLUME ${HOME}
ENTRYPOINT ["./container-entrypoint.sh"]
CMD ["./run.sh"]
USER 1000
