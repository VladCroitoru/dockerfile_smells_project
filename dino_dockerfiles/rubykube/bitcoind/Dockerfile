FROM ubuntu:xenial

ARG users=btc_user

# Create bitcoin user
ENV HOME /bitcoin

RUN groupadd -g 1000 bitcoin \
    && useradd -u 1000 -g bitcoin -s /bin/bash -m -d ${HOME} bitcoin

# Install bitcoind packages
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C70EF1F0305A1ADB9986DBD8D46F45428842CE5E && \
    echo "deb http://ppa.launchpad.net/bitcoin/bitcoin/ubuntu xenial main" > /etc/apt/sources.list.d/bitcoin.list

RUN apt-get update && apt-get install -y bitcoind
RUN apt-get install -y wget curl python

# Install RPCUser: it will generate `-rpcauth` for bitcoind

RUN wget https://raw.githubusercontent.com/bitcoin/bitcoin/master/share/rpcuser/rpcuser.py \
    -O /usr/bin/rpcuser.py \
    && chmod +x /usr/bin/rpcuser.py

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ADD bin/gen_rpc_auth /usr/bin

# Prepare bitcoin config
RUN mkdir ${HOME}/.bitcoin
ADD config/bitcoin.conf ${HOME}/.bitcoin
RUN chown bitcoin:bitcoin -R $HOME

USER bitcoin

# Create rpc users
# RUN sh -c "gen_rpc_auth ${users}"

EXPOSE 19000 19001

CMD ["bitcoind"]
