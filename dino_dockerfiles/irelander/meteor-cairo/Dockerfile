FROM amazonlinux:2016.09
MAINTAINER Irelander Kai

ENV METEORD_DIR /opt/meteord
COPY scripts $METEORD_DIR

ARG NODE_VERSION
ENV NODE_VERSION ${NODE_VERSION:-4.8.4}
ONBUILD ENV NODE_VERSION ${NODE_VERSION:-4.8.4}

RUN bash $METEORD_DIR/lib/install_base.sh
RUN bash $METEORD_DIR/lib/install_node.sh
RUN bash $METEORD_DIR/lib/install_phantomjs.sh
RUN bash $METEORD_DIR/lib/cleanup.sh

EXPOSE 80
ENTRYPOINT bash $METEORD_DIR/run_app.sh