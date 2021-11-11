FROM jeanblanchard/alpine-glibc

# create user qtum and add to group qtum
RUN addgroup -S qtum && adduser -S -g qtum qtum

# install wget to use later in this file
RUN set -ex \
	&& apk add --no-cache wget su-exec \
	&& rm -rf /var/lib/apt/lists/*

# set ENV variables to call later in this file
ENV QTUM_VERSION 1.0.2
ENV QTUM_URL https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.0.2/qtum-0.14.3-x86_64-linux-gnu.tar.gz

# install qtum binaries
RUN set -ex \
	&& cd /tmp \
	&& wget --no-check-certificate -qO qtum.tar.gz "$QTUM_URL" \
	&& tar -xzvf qtum.tar.gz -C /usr/local --strip-components=1 --exclude=qtum-qt --exclude=test_qtum \
	&& rm -rf /tmp/*

# set variable for location of data storage in docker iameg AND 
# create data directory and give owner permissions to user qtum and group qtum
ENV QTUM_DATA /data
RUN mkdir "$QTUM_DATA" \
	&& chown -R qtum:qtum "$QTUM_DATA" \
	&& ln -sfn "$QTUM_DATA" /home/qtum/.qtum \
	&& chown -h qtum:qtum /home/qtum/.qtum
VOLUME /data

# copy entrypoint.sh to to docker image and start by executing the entrypoint.sh file 
COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Make these ports available to the world outside of this container
EXPOSE 3888 3889 13888 13889 23888
