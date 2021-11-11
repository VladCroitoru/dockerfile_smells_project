FROM openjdk:7-jre-alpine

# Fix to NPE sun.awt.X11FontManager.getDefaultPlatformFont
# https://github.com/metabase/metabase/commit/9c9acc36d458ca3a81a2c4224a23bc51740b9e69 
RUN apk update && apk add fontconfig ttf-dejavu
ENV FC_LANG en-US
ENV LC_CTYPE en_US.UTF-8

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# let "Tomcat Native" live somewhere isolated
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR

RUN apk add --no-cache gnupg

# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS
# see also "update.sh" (https://github.com/docker-library/tomcat/blob/master/update.sh)
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6 07E48665A34DCAFAE522E5E6266191C37C037D42 47309207D818FFD8DCD3F83F1931D684307A10A5 541FBE7D8F78B25E055DDEE13C370389288584E7 61B832AC2F1C5A90F0F9B00A1C506407564C17A3 713DA88BE50911535FE716F5208B0AB1D63011C7 79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED 9BA44C2621385CB966EBA586F72C284D731FABEE A27677289986DB50844682F8ACB77FC2E86E29AC A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23
RUN set -ex; \
	for key in $GPG_KEYS; do \
		gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done

ENV TOMCAT_MAJOR 7
ENV TOMCAT_VERSION 7.0.79

# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
ENV TOMCAT_TGZ_URL https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
# not all the mirrors actually carry the .asc files :'(
ENV TOMCAT_ASC_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz.asc

RUN set -x \
	\
	&& apk add --no-cache --virtual .fetch-deps \
		ca-certificates \
		tar \
		openssl \
	&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \
	&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \
	&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz* \
	\
	&& nativeBuildDir="$(mktemp -d)" \
	&& tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" --strip-components=1 \
	&& apk add --no-cache --virtual .native-build-deps \
		apr-dev \
		coreutils \
		dpkg-dev dpkg \
		gcc \
		libc-dev \
		make \
		"openjdk${JAVA_VERSION%%[-~bu]*}"="$JAVA_ALPINE_VERSION" \
		openssl-dev \
	&& ( \
		export CATALINA_HOME="$PWD" \
		&& cd "$nativeBuildDir/native" \
		&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
		&& ./configure \
			--build="$gnuArch" \
			--libdir="$TOMCAT_NATIVE_LIBDIR" \
			--prefix="$CATALINA_HOME" \
			--with-apr="$(which apr-1-config)" \
			--with-java-home="$(docker-java-home)" \
			--with-ssl=yes \
		&& make -j "$(nproc)" \
		&& make install \
	) \
	&& runDeps="$( \
		scanelf --needed --nobanner --recursive "$TOMCAT_NATIVE_LIBDIR" \
			| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
			| sort -u \
			| xargs -r apk info --installed \
			| sort -u \
	)" \
	&& apk add --virtual .tomcat-native-rundeps $runDeps \
	&& apk del .fetch-deps .native-build-deps \
	&& rm -rf "$nativeBuildDir" \
	&& rm bin/tomcat-native.tar.gz

# verify Tomcat Native is working properly
RUN set -e \
	&& nativeLines="$(catalina.sh configtest 2>&1)" \
	&& nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \
	&& nativeLines="$(echo "$nativeLines" | sort -u)" \
	&& if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat Native library' >&2; then \
		echo >&2 "$nativeLines"; \
		exit 1; \
	fi

################################## Apache2 ##############################
# ensure www-data user exists
RUN set -x \
&& addgroup -g 82 -S www-data \
&& adduser -u 82 -D -S -G www-data www-data
# 82 is the standard uid/gid for "www-data" in Alpine
# http://git.alpinelinux.org/cgit/aports/tree/main/apache2/apache2.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/lighttpd/lighttpd.pre-install?h=v3.3.2
# http://git.alpinelinux.org/cgit/aports/tree/main/nginx-initscripts/nginx-initscripts.pre-install?h=v3.3.2

ENV HTTPD_PREFIX /usr/local/apache2
ENV PATH $HTTPD_PREFIX/bin:$PATH
RUN mkdir -p "$HTTPD_PREFIX" \
&& chown www-data:www-data "$HTTPD_PREFIX"
WORKDIR $HTTPD_PREFIX

ENV HTTPD_VERSION 2.4.25
ENV HTTPD_SHA1 bd6d138c31c109297da2346c6e7b93b9283993d2

# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
ENV HTTPD_BZ2_URL http://archive.apache.org/dist/httpd/$HTTPD_VERSION.tar.bz2
# not all the mirrors actually carry the .asc files :'(
ENV HTTPD_ASC_URL https://www.apache.org/dist/httpd/httpd-$HTTPD_VERSION.tar.bz2.asc

# if the version is outdated, we have to pull from the archive :/

ENV HTTPD_BZ2_FALLBACK_URL https://archive.apache.org/dist/httpd/httpd-$HTTPD_VERSION.tar.bz2
ENV HTTPD_ASC_FALLBACK_URL https://archive.apache.org/dist/httpd/httpd-$HTTPD_VERSION.tar.bz2.asc

# see https://httpd.apache.org/docs/2.4/install.html#requirements
RUN set -x \
&& runDeps=' \
	apr-dev \
	apr-util-dev \
	apr-util-ldap \
	perl \
' \
&& apk add --no-cache --virtual .build-deps \
	$runDeps \
	ca-certificates \
	coreutils \
	dpkg-dev dpkg \
	gcc \
	gnupg \
	libc-dev \
	# mod_session_crypto
	libressl \
	libressl-dev \
	# mod_proxy_html mod_xml2enc
	libxml2-dev \
	# mod_lua
	lua-dev \
	make \
	# mod_http2
	nghttp2-dev \
	pcre-dev \
	tar \
	# mod_deflate
	zlib-dev \
\
&& { \
	wget -O httpd.tar.bz2 "$HTTPD_BZ2_URL" \
	|| wget -O httpd.tar.bz2 "$HTTPD_BZ2_FALLBACK_URL" \
; } \
&& echo "$HTTPD_SHA1 *httpd.tar.bz2" | sha1sum -c - \
# see https://httpd.apache.org/download.cgi#verify
&& { \
	wget -O httpd.tar.bz2.asc "$HTTPD_ASC_URL" \
	|| wget -O httpd.tar.bz2.asc "$HTTPD_ASC_FALLBACK_URL" \
; } \
&& export GNUPGHOME="$(mktemp -d)" \
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys A93D62ECC3C8EA12DB220EC934EA76E6791485A8 \
&& gpg --batch --verify httpd.tar.bz2.asc httpd.tar.bz2 \
&& rm -rf "$GNUPGHOME" httpd.tar.bz2.asc \
\
&& mkdir -p src \
&& tar -xf httpd.tar.bz2 -C src --strip-components=1 \
&& rm httpd.tar.bz2 \
&& cd src \
\
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
&& ./configure \
	--build="$gnuArch" \
	--prefix="$HTTPD_PREFIX" \
	--enable-mods-shared=reallyall \
&& make -j "$(nproc)" \
&& make install \
\
&& cd .. \
&& rm -r src man manual \
\
&& sed -ri \
	-e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \
	-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \
	"$HTTPD_PREFIX/conf/httpd.conf" \
\
&& runDeps="$runDeps $( \
	scanelf --needed --nobanner --recursive /usr/local \
		| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
		| sort -u \
		| xargs -r apk info --installed \
		| sort -u \
)" \
&& apk add --virtual .httpd-rundeps $runDeps \
&& apk del .build-deps

RUN mkdir -p /logs && ln -s /usr/local/tomcat/logs /logs/tomcat && ln -s /usr/local/apache2/logs /logs/apache2

EXPOSE 80 443

COPY run.sh /usr/local/bin
RUN chmod +x /usr/local/bin/run.sh

CMD ["run.sh"]
