FROM alpine:3.4

RUN  apk add --no-cache --update --virtual=.build-group-1 curl bash postgresql-client jq python py-pip wget &&\
     apk add --no-cache --update --virtual=.git git &&\
     pip install --upgrade pip &&\
     pip install python-dateutil &&\
     git clone -b v1.6.1 --single-branch  https://github.com/s3tools/s3cmd.git /opt/s3cmd &&\
     rm -rf /opt/s3cmd/.git &&\
     ln -s /opt/s3cmd/s3cmd /usr/bin/s3cmd &&\
     apk del .git
ADD s3cfg /root/.s3cfg

CMD ["/usr/bin/curl"]

