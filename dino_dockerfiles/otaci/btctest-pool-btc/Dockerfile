FROM alpine
MAINTAINER Otaci <otaci@protonmail.com>

ARG USER_ID
ARG GROUP_ID

ENV HOME /eloipool

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

WORKDIR /eloipool

# install eloipool
RUN apk --no-cache upgrade \
	&& apk --no-cache add python3=3.6.1-r2 git \
	&& cd /eloipool \
	&& git clone https://github.com/jgarzik/python-bitcoinrpc.git \
	&& git clone https://gitorious.org/bitcoin/python-base58.git \
	&& git clone https://gitorious.org/bitcoin/eloipool.git 

RUN cd /eloipool/eloipool \
	&& ln -s ../python-base58/base58.py base58.py \
	&& ln -s ../python-bitcoinrpc/bitcoinrpc/ bitcoinrpc \
	&& ln -s ../python-bitcoinrpc/jsonrpc/ jsonrpc


# cleanup
RUN rm -rf /tmp/* /var/tmp/* 

ADD ./bin /usr/local/bin

EXPOSE 3334
CMD run-eloipool.sh
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

