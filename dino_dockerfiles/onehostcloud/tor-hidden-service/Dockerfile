FROM onehostcloud/docker-tor
MAINTAINER OneHost Cloud <info@onehostcloud.hosting>

RUN mkdir -p /var/lib/tor/hidden-service
RUN chown -R root:root /var/lib/tor/hidden-service
RUN chmod -R 600 /var/lib/tor/hidden-service
VOLUME /var/lib/tor/hidden-service

ADD ./torrc /etc/torrc
ADD ./start-tor /bin/start-tor

CMD /bin/start-tor
