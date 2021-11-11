
FROM ubuntu:18.04


RUN apt-get update -y && apt-get upgrade -y && apt-get install cron python2.7 python-pip git-core software-properties-common -y && add-apt-repository -y ppa:bitcoin/bitcoin
RUN apt-get install curl build-essential libtool automake autoconf autotools-dev autoconf pkg-config libssl-dev libgmp3-dev libevent-dev bsdmainutils libboost-all-dev libzmq3-dev libminiupnpc-dev libdb4.8-dev libdb4.8++-dev -y
RUN apt-get install bsdmainutils -y



ENV PORT 18888

WORKDIR /root/

RUN git clone https://github.com/absolute-community/absolute.git
RUN cd absolute && chmod -R 777 * && ./autogen.sh && ./configure --disable-tests --disable-gui-tests && make && make install

RUN git clone https://github.com/absolutecrypto/sentinel.git /root/sentinel
RUN pip2 install -r /root/sentinel/requirements.txt
RUN echo "absolute_conf=/root/config.conf" >> /root/sentinel/sentinel.conf
RUN echo "* * * * * root cd /root/sentinel && /usr/bin/python bin/sentinel.py >/dev/null 2>&1" >> /etc/crontab
RUN crontab /etc/crontab



ADD run.sh /usr/local/bin
RUN chmod +x /usr/local/bin/run.sh

ENTRYPOINT ["/usr/local/bin/run.sh"]
CMD []
