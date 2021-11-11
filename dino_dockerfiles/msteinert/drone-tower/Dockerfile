FROM alpine:3.2

RUN apk add -U \
	ca-certificates \
	python3 \
 && rm -rf /var/cache/apk/*

ADD ./ /tmp/drone-tower
RUN cd /tmp/drone-tower \
 && python3 setup.py install \
 && rm -rf /tmp/drone-tower

ENTRYPOINT ["drone-tower"]
