FROM gliderlabs/alpine:3.3

RUN apk --update add python py-pip openssl ca-certificates git tcpdump
RUN apk --update add --virtual build-dependencies python-dev build-base wget && \
	git clone https://github.com/nimia/public_drown_scanner.git /app && \
	cd /app && \
  	pip install enum pycrypto scapy pyasn1 && \
	apk del build-dependencies

WORKDIR /app

COPY resources/ssl_tls_crypto.py scapy-ssl_tls/

ENTRYPOINT ["python", "scanner.py"]

CMD ["google.com", "443"]