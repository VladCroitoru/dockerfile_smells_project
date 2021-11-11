FROM alpine
ENTRYPOINT ["/bin/sh"]

RUN apk add --update openssl && \
	apk upgrade

ENV PORT=8888

ADD ./openssl_ocspd.sh /openssl_ocspd.sh

RUN chmod +x /openssl_ocspd.sh

CMD ["./openssl_ocspd.sh"]
