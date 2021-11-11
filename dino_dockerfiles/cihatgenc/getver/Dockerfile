FROM alpine

ENV TMPDIR /tmp

RUN mkdir /opt && \
	apk add --update ca-certificates && \
	update-ca-certificates

RUN wget -O /opt/getver https://dl.dropboxusercontent.com/u/48462121/getver_linux_amd64 && \
	chmod +x /opt/getver

EXPOSE 9080

CMD ["/opt/getver"]