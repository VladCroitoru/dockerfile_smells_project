FROM mysql:5.7.12

RUN apt-get update

RUN apt-get install -y git

ENV BIN_DIR=/usr/local/bin/classic-db
ENV CONFIG_DIR=/etc/classicdb

RUN useradd -r updater
RUN mkdir -p $BIN_DIR
RUN chown updater:updater $BIN_DIR

RUN mkdir -p $CONFIG_DIR
RUN chown updater:updater $CONFIG_DIR

USER updater

RUN git clone https://github.com/classicdb/database.git $BIN_DIR

COPY entrypoint.sh /usr/local/bin/

WORKDIR $BIN_DIR

ENTRYPOINT ["entrypoint.sh"]
