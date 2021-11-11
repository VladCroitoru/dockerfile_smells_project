FROM debian:8
MAINTAINER <jeroen@peetersweb.nl>

ENV METEORD_DIR /opt/meteord
ENV RELEASE "1.4.3.1"

RUN apt-get -y update; apt-get install -y xz-utils

COPY scripts $METEORD_DIR

RUN bash $METEORD_DIR/init.sh
RUN bash $METEORD_DIR/install-meteor.sh

ENTRYPOINT bash $METEORD_DIR/run_app.sh

WORKDIR /app
ONBUILD ADD ./ .
ONBUILD RUN npm install
ONBUILD RUN bash $METEORD_DIR/lib/build_app.sh

EXPOSE 80
