############################################################
# Dockerfile to run an OrientDB (Graph) Container
############################################################
FROM orientdb:2.1.25

EXPOSE 2434

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

# Compile and install monit and confd
# ENV MONIT_VERSION=5.19.0 \
#     MONIT_HOME=/opt/monit \
#     MONIT_URL=https://mmonit.com/monit/dist \
#     SERVICE_VOLUME=/opt/tools \
#     PATH=$PATH:/opt/monit/bin

# # Compile and install monit
# RUN apk add --update gcc musl-dev make openssl-dev && \
#     mkdir -p /opt/src; cd /opt/src && \
#     curl -sS ${MONIT_URL}/monit-${MONIT_VERSION}.tar.gz | gunzip -c - | tar -xf - && \
#     cd /opt/src/monit-${MONIT_VERSION} && \
#     ./configure  --prefix=${MONIT_HOME} --without-pam && \
#     make && make install && \
#     mkdir -p ${MONIT_HOME}/etc/conf.d ${MONIT_HOME}/log && \
#     apk del gcc musl-dev make openssl-dev &&\
#     rm -rf /var/cache/apk/* /opt/src

ADD orient_service.sh /orientdb/orient_service.sh
ADD run.sh /orientdb/run.sh

# COPY monitrc /etc/monitrc
# RUN chmod 0700 /etc/monitrc \
#     && chmod +x /orientdb/orient_service.sh \
#     && chmod +x /orientdb/run.sh
RUN chmod +x /orientdb/orient_service.sh \
    && chmod +x /orientdb/run.sh

VOLUME ["/data/status"]

# Default command start the server
CMD ["/orientdb/run.sh"]
