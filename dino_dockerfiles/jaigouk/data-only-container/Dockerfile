FROM debian:jessie
MAINTAINER "Jaigouk Kim" <ping@jaigouk.kim>

RUN echo "crete lab80 user and directories" \
    && useradd lab80
    && mkdir /data
    && chown -R lab80:lab80 /data


USER lab80

RUN echo "copy files"
COPY forever.sh /usr/local/bin/
ADD db /data/db
ADD droneio /data/droneio
ADD jenkins /data/jenkins

VOLUME ["/data"]

ENTRYPOINT ["/usr/local/bin/forever.sh"]