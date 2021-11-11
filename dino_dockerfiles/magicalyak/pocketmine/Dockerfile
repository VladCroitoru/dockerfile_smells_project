# Minecraft PE Server
FROM phusion/baseimage:bionic-1.0.0

LABEL maintainer="Tom Gamull <tom.gamull@gmail.com>"
LABEL build_date="2020-07-26"

ARG BDS_Version=latest
ENV VERSION=$BDS_Version

# Secure and init
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh
#CMD ["/sbin/my_init"]

# Update, Install Prerequisites
RUN apt-get -y update && \
    apt-get install -y \
	unzip \
	curl \
        wget \
        libxml2-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir /data && \
    groupadd -g 1000 minecraft && \
    useradd -u 1000 -g 1000 -r minecraft

# Stage Files
RUN  if [ "$VERSION" = "latest" ] ; then \
        LATEST_VERSION=$( \
            curl -v --silent  https://www.minecraft.net/en-us/download/server/bedrock/ 2>&1 | \
            grep -o 'https://minecraft.azureedge.net/bin-linux/[^"]*' | \
            sed 's#.*/bedrock-server-##' | sed 's/.zip//') && \
        export VERSION=$LATEST_VERSION && \
        echo "Setting VERSION to $LATEST_VERSION" ; \
    else echo "Using VERSION of $VERSION"; \
    fi && \
    curl https://minecraft.azureedge.net/bin-linux/bedrock-server-${VERSION}.zip --output bedrock-server.zip

ADD start.sh /opt/start.sh
RUN chown -R minecraft:minecraft /data && chmod +x /opt/start.sh

USER minecraft:minecraft
RUN cd /data

VOLUME /data
WORKDIR /data

# Setup container
EXPOSE 19132/udp

# Start Pocketmine
CMD ["/opt/start.sh"]
