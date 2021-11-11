FROM alpine:3.5
RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/*
ADD list.txt /
RUN mkdir -p /root/.gazebo/models && \
    for i in $(cat /list.txt); do \
        wget http://models.gazebosim.org/$i/model.tar.gz -P /tmp -q \
        && tar xvzf /tmp/model.tar.gz -C /root/.gazebo/models \
        && rm /tmp/model.tar.gz \
    ; done
VOLUME /root/.gazebo/models
CMD exec /bin/sh -c "while true; do sleep 30; done;"