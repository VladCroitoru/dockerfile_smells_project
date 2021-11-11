FROM mariadb:10.1

ENV HUGE_VERSION 3.1

RUN set -x \
	&& apt-get update && apt-get install --no-install-recommends -y \
		curl openssl ca-certificates \
	&& curl -L https://github.com/panique/huge/archive/v$HUGE_VERSION.tar.gz \
		-o $HUGE_VERSION.tar.gz \
	&& tar -zxf $HUGE_VERSION.tar.gz \
	&& mv huge-$HUGE_VERSION/application/_installation/*.sql docker-entrypoint-initdb.d/ \
	&& apt-get purge --auto-remove -y curl openssl ca-certificates \
	&& rm -rf $HUGE_VERSION.tar.gz huge-$HUGE_VERSION.tar.gz \
		/var/lib/apt/lists/* \

CMD ["mysqld"]
