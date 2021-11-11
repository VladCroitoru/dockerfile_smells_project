FROM debian
COPY run.sh /run.sh
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g'  /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends \
	bluez \
	curl \
	ca-certificates \
	&& rm -rf /var/lib/apt/lists/* \
	&& chmod a+x /run.sh

CMD [ "/run.sh" ]