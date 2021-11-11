FROM debian:sid

## <http://docs.mongodb.org/manual/tutorial/install-mongodb-on-debian/>
## <https://github.com/nodesource/distributions>
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/* && \
    chmod go+w /tmp

RUN npm install amid

RUN curl -O http://downloads.mongodb.org/linux/mongodb-linux-x86_64-3.0.0.tgz && \
    tar zvxf mongodb-linux-x86_64-3.0.0.tgz && \
    mv mongodb-linux-x86_64-3.0.0 mongodb && \
    rm -fr mongodb-linux-x86_64-3.0.0.tgz && \
    mkdir -p /data/db && \
    chmod go+w /data/db

ADD server.sh /server
ADD mongodb.conf /mongodb.conf
ADD amid-config.json /config.json
RUN chmod u+x /server
