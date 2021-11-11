FROM java:8

RUN rm -vfr /var/lib/apt/lists/* && apt-get clean && apt-get update && apt-get install -y --force-yes --no-install-recommends \
        xvfb \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app
ENV FAKESMTP_VERSION "1.13"
RUN wget http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-${FAKESMTP_VERSION}.zip
RUN unzip fakeSMTP-${FAKESMTP_VERSION}.zip
VOLUME ["/mails"]
EXPOSE 25
ADD entrypoint.sh /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["-s", "-b", "-o", "/mails"]
