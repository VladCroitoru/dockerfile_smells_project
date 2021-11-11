from ncarlier/mqtt

ENV TINI_VERSION v0.10.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

ENV MOSQUITTO_HOME /etc/mosquitto

COPY ./mosquitto.conf $MOSQUITTO_HOME

VOLUME ["/etc/mosquitto/conf.d"]
CMD ["mosquitto", "-c", "/etc/mosquitto/mosquitto.conf"]

