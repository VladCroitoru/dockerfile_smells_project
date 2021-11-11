# Build BadVPN from source
FROM ubuntu:latest AS badvpn
ENV DEBIAN_FRONTEND="noninteractive"
RUN apt update && apt -qq install --reinstall -y cmake make build-essential git pkg-config cmake-data
RUN git clone https://github.com/OFVp-Project/badvpn.git /tmp/badvpn
RUN mkdir /tmp/build /tmp/output && cd /tmp/build/ && \
  cmake /tmp/badvpn -DBUILD_NOTHING_BY_DEFAULT=1 -DBUILD_UDPGW=1 -DCMAKE_INSTALL_PREFIX=/tmp/output && \
  make install

# Servers
FROM ubuntu:latest AS servers
ENV DEBIAN_FRONTEND="noninteractive"
LABEL name="OFVp Server"
LABEL org.opencontainers.image.title="OFVp Server"
LABEL org.opencontainers.image.description="Start a server for Http Injector in the fastest and easiest way to maintain and update as new tools are released and your host does not need to restart with all new changes."
LABEL org.opencontainers.image.vendor="Sirherobrine23"
LABEL org.opencontainers.image.licenses="mit"
LABEL org.opencontainers.image.source="https://github.com/OFVp-Project/Server"

# Ports
EXPOSE 22/tcp 80/tcp 7300/tcp 51820/udp 3000/tcp 8081/tcp

# Install Core Packages
RUN apt update && apt -y install build-essential wget curl git unzip zip zsh sudo jq screen nano ca-certificates net-tools bc lsof dos2unix nload zlib1g-dev ifupdown iputils-ping iproute2 tzdata openssl ntp procps openresolv inotify-tools gnupg libc6 libelf-dev perl pkg-config figlet python3 python python3-pip

# Change bash to zsh
RUN usermod --shell /usr/bin/zsh root

# Install Squid, Openssh
RUN apt update && apt install -y squid openssh-server && \
rm -fv /etc/ssh/sshd_config /etc/ssh/ssh_host_* /etc/squid*/squid.conf

# Install Wireguard
RUN apt-get -y install debconf-utils && \
echo resolvconf resolvconf/linkify-resolvconf boolean false | debconf-set-selections && \
apt-get -y install resolvconf && \
apt -y install wireguard-tools iptables iproute2 resolvconf qrencode dkms wireguard

# Install badVPN
COPY --from=badvpn /tmp/output/bin/badvpn-udpgw /bin/badvpn-udpgw

# Copy and Install Dependecies
WORKDIR /usr/src/Backend

# Install latest NodeJS
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && apt install -y nodejs && npm install -g npm@latest

# Copy Backend Control
COPY package*.json ./
RUN npm install --no-save
COPY ./ ./

# Set Entrypoint
ENTRYPOINT [ "node", "--no-warnings", "index.js" ]
