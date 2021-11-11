FROM counterparty/base

MAINTAINER Counterparty Developers <dev@counterparty.io>

# Install extra dependencies
RUN apt-get update && apt-get -y install python python-pip

# Download and install armory
ENV ARMORY_VER="0.93.3_ubuntu-64bit"
RUN apt-get update && apt-get -y install xvfb python-qt4 python-twisted python-psutil xdg-utils hicolor-icon-theme
RUN wget -O /tmp/armory.deb https://www.bitcoinarmory.com/downloads/bitcoinarmory-releases/armory_${ARMORY_VER}.deb
# bug fix (see http://askubuntu.com/a/406015)
RUN mkdir -p /usr/share/desktop-directories/
RUN dpkg -i /tmp/armory.deb && rm /tmp/armory.deb
RUN mkdir /root/.armory

# Bitcoin datadir must be mounted in the container as /root/bitcoin_data`
RUN mkdir /bitcoin_data
    
# Install
COPY . /armory-utxsvr
WORKDIR /armory-utxsvr
RUN pip2 install -r requirements.txt
RUN python2 setup.py develop

COPY docker/start.sh /usr/local/bin/start.sh
RUN chmod a+x /usr/local/bin/start.sh

EXPOSE 6590 6591

# NOTE: Defaults to running on mainnet, specify -e TESTNET=1 to start up on testnet
ENTRYPOINT ["start.sh"]
