FROM alpine:latest

ENV SYNC_DIR /svn
ENV SYNC_INT 30

RUN apk update --no-cache  \
	&& apk add subversion ca-certificates
	
VOLUME /svn

COPY sync.sh /sync.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /sync.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD [ "/sync.sh" ]