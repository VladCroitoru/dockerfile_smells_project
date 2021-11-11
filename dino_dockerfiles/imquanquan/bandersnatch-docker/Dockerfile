FROM alpine:latest

RUN apk update && apk add --no-cache ca-certificates dcron bash  python3 tzdata&& \
	rm -rf /var/cache/apk/* && \
        ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
        echo "Asia/Shanghai" > /etc/timezone && \
	pip3 install -r https://bitbucket.org/pypa/bandersnatch/raw/stable/requirements.txt && \
	touch /var/log/pypi.log  && \
	mkdir /mirrors

ADD root /etc/crontabs/root
ADD bandersnatch.conf /etc/bandersnatch.conf

CMD crond && tail -f /var/log/pypi.log
