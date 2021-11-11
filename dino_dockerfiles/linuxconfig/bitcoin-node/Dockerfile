FROM debian:9

MAINTAINER Lubos Rendek <web@linuxconfig.org>

RUN apt-get update
RUN apt-get install -y wget

# Install bitcoin daemon
RUN wget -q https://bitcoin.org/bin/bitcoin-core-0.14.2/bitcoin-0.14.2-x86_64-linux-gnu.tar.gz
RUN tar xzf bitcoin-0.14.2-x86_64-linux-gnu.tar.gz
RUN install -m 0755 -o root -g root -t /usr/local/bin bitcoin-0.14.2/bin/*; mkdir /root/.bitcoin/

# Include bitcoind statup script to configure and start bitcoin daemon
ADD start-node.sh /
RUN chmod 755 start-node.sh

# Clean up
RUN rm -fr bitcoin-0.14.2 bitcoin-0.14.2-x86_64-linux-gnu.tar.gz

EXPOSE 8332 8333

CMD ["/start-node.sh"]



