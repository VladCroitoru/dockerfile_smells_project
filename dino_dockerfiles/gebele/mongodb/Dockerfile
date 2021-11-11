FROM alpine:edge
LABEL maintainer="gebele@in-silico.ch"
LABEL io.openrisknet.tags mongodb
LABEL io.openrisknet.non-scalable true
LABEL io.openshift.expose-services 27027
LABEL io.openrisknet.min-memory 4Gi
LABEL io.openrisknet.min-cpu 2
RUN apk add --no-cache mongodb

VOLUME /data/db
EXPOSE 27017 27017

#COPY run.sh /root
#ENTRYPOINT [ "/root/run.sh" ]
#test
CMD [ "mongod" ]
