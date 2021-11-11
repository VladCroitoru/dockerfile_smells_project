FROM qnib/alplain-init:edge

RUN echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
 && apk add --no-cache mongodb \
 && rm /usr/bin/mongosniff /usr/bin/mongoperf
VOLUME ["/data/db/"]
ADD opt/qnib/mongodb/bin/start.sh /opt/qnib/mongodb/bin/
CMD ["/opt/qnib/mongodb/bin/start.sh"]
