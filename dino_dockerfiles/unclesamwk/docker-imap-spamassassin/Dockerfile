FROM ubuntu

ENV DEBIAN_FRONTEND noninteractive

ENV TZ=Europe/Berlin

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone && \
    apt-get -qq update && \
    apt-get -y install spamassassin imapfilter python3 razor pyzor unp python3-pip python3-setuptools wget unzip rsyslog && \
    pip3 install --upgrade pip && \
    pip3 install isbg && \
    mkdir /root/.spamassassin && \
    apt-get autoremove --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    python3 --version

COPY user_prefs /root/.spamassassin/user_prefs
COPY default_spamassassin /etc/default/spamassassin
COPY start.sh /start.sh
COPY cron_spamassassin /etc/cron.daily/spamassassin

CMD cron && bash /start.sh
