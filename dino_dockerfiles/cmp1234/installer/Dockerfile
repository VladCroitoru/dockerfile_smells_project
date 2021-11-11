FROM cmp1234/python-jre:2.7.15-8u181-alpine3.8-sp01

COPY build_openssh.sh /build_openssh.sh 

RUN set -ex; \
 chmod +x /build_openssh.sh; \
 apk add --no-cache --virtual .build-deps \
		coreutils \
		gcc \
		curl \
		linux-headers \
		make \
		python2-dev \
		python3-dev \
		musl-dev \
		zlib \
		zlib-dev \
		openssl==1.0.2p-r0 \
		openssl-dev==1.0.2p-r0 \
		perl \
		libffi \
		libffi-dev; \
  apk add --no-cache curl libcrypto1.0 sshpass python tar; \
  curl -ko /usr/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.10.0/bin/linux/amd64/kubectl; \
  chmod +x /usr/bin/kubectl; \
  /build_openssh.sh; \
  rm -f /build_openssh.sh; \
  deps=' \
            pycrypto==2.6.1 \
            paramiko==1.17.6 \
            click==6.7 \
            Jinja2==2.8 \
            PyYAML==3.11 \
	    ansible==2.4.1.0 \
	    pexpect==4.2.1 \
	    docker \
	    pyaml \
	    zabbix-api==0.5.3 \
        '; \
  pip install $deps; \
  apk del .build-deps;
