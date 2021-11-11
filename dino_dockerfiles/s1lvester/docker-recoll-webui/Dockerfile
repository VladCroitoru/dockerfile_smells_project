FROM debian:jessie

ADD start.sh /root/
ADD bgindex.sh /root/

RUN echo deb http://www.lesbonscomptes.com/recoll/debian/ jessie main > \
	/etc/apt/sources.list.d/recoll.list &&\
    echo deb-src http://www.lesbonscomptes.com/recoll/debian/ jessie main >> \
	/etc/apt/sources.list.d/recoll.list &&\
    apt-get -qq update && \
    apt-get -qq --force-yes install \
        recoll python-recoll \
        python git wv \
        aspell aspell-de aspell-en \
        pdftk \
        poppler-utils && \
    apt-get autoremove && apt-get clean &&\
    mkdir /data && mkdir -p /root/.recoll &&\
    git clone https://github.com/koniu/recoll-webui.git &&\
    chmod +x /root/start.sh && chmod +x /root/bgindex.sh

ADD recoll.conf /root/.recoll/recoll.conf

CMD ["/root/start.sh"]
