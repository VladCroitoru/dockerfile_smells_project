FROM centos:latest

# Update to the latest
RUN yum update -y && yum install -y ca-certificates \
		curl \
		wget \
		bzip2 \
		unzip \
		xz-utils \
		which \
	&& rm -rf /var/lib/yum/repos/*

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

# add a simple script that can auto-detect the appropriate JAVA_HOME value
# based on whether the JDK or only the JRE is installed
RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home

ENV JAVA_VERSION 1.8.0.131
ENV JAVA_CENTOS_VERSION 2.b11.el7_3

# do some fancy footwork to create a JAVA_HOME that's cross-architecture-safe
RUN ln -svT "/usr/lib/jvm/java-1.8.0-openjdk-$JAVA_VERSION-$JAVA_CENTOS_VERSION.$(uname -m)" /docker-java-home
ENV JAVA_HOME /docker-java-home/jre

RUN set -ex; \
	\
	yum update -y; \
	yum install -y \
		java-1.8.0-openjdk-headless-"$JAVA_VERSION"-"$JAVA_CENTOS_VERSION" \
		java-1.8.0-openjdk-devel-"$JAVA_VERSION"-"$JAVA_CENTOS_VERSION" \
	; \
	rm -rf /var/lib/yum/repos/*;

# Install tomcat

ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
RUN mkdir -p "$CATALINA_HOME"
WORKDIR $CATALINA_HOME

# let "Tomcat Native" live somewhere isolated
ENV TOMCAT_NATIVE_LIBDIR $CATALINA_HOME/native-jni-lib
ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}$TOMCAT_NATIVE_LIBDIR

# see https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/KEYS
# see also "update.sh" (https://github.com/docker-library/tomcat/blob/master/update.sh)
ENV GPG_KEYS 05AB33110949707C93A279E3D3EFE6B686867BA6 07E48665A34DCAFAE522E5E6266191C37C037D42 47309207D818FFD8DCD3F83F1931D684307A10A5 541FBE7D8F78B25E055DDEE13C370389288584E7 61B832AC2F1C5A90F0F9B00A1C506407564C17A3 713DA88BE50911535FE716F5208B0AB1D63011C7 79F7026C690BAA50B92CD8B66A3AD3F4F22C4FED 9BA44C2621385CB966EBA586F72C284D731FABEE A27677289986DB50844682F8ACB77FC2E86E29AC A9C5DF4D22E99998D9875A5110C01C5A2F6059E7 DCFD35E0BF8CA7344752DE8B6FB21E8933C60243 F3A04C595DB5B6A5F1ECA43E3B7BBB100D811BBE F7DA48BB64BCB84ECBA7EE6935CD23C10D498E23
RUN set -ex; \
	for key in $GPG_KEYS; do \
		# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
		gpg --keyserver	keyserver.ubuntu.com --recv-keys "$key"; \
	done

ENV TOMCAT_MAJOR 8
ENV TOMCAT_VERSION 8.5.15
ENV OPENSSL_VERSION 1.0.2k

# runtime dependencies for Tomcat Native Libraries
# Tomcat Native 1.2+ requires a newer version of OpenSSL than debian:jessie has available
# > checking OpenSSL library version >= 1.0.2...
# > configure: error: Your version of OpenSSL is not compatible with this version of tcnative
# see http://tomcat.10.x6.nabble.com/VOTE-Release-Apache-Tomcat-8-0-32-tp5046007p5046024.html (and following discussion)
# and https://github.com/docker-library/tomcat/pull/31
# https://issues.apache.org/jira/browse/INFRA-8753?focusedCommentId=14735394#comment-14735394
ENV TOMCAT_TGZ_URL https://www.apache.org/dyn/closer.cgi?action=download&filename=tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz
# not all the mirrors actually carry the .asc files :'(
ENV TOMCAT_ASC_URL https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-tomcat-$TOMCAT_VERSION.tar.gz.asc
ENV OPENSSL_URL https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz

RUN set -x \
	\
	&& yum install -y \
	   perl \
       tar \
       gcc \
       make \
       glibc-common \
	   apr-devel \
	&& wget -O openssl.tar.gz "$OPENSSL_URL" \
	&& tar -xvf openssl.tar.gz \
	&& ( \
	   cd openssl-"$OPENSSL_VERSION" \
	   && ./config -fPIC\
	   && make \
	   && make test \
	   && make install \
	   && cd .. \
	   && rm -rf openssl* \
	) \
	&& wget -O tomcat.tar.gz "$TOMCAT_TGZ_URL" \
	&& wget -O tomcat.tar.gz.asc "$TOMCAT_ASC_URL" \
	&& gpg --batch --verify tomcat.tar.gz.asc tomcat.tar.gz \
	&& tar -xvf tomcat.tar.gz --strip-components=1 \
	&& rm bin/*.bat \
	&& rm tomcat.tar.gz* \
	\
	&& nativeBuildDir="$(mktemp -d)" \
	&& tar -xvf bin/tomcat-native.tar.gz -C "$nativeBuildDir" --strip-components=1 \
	&& ( \
		export CATALINA_HOME="$PWD" \
		&& cd "$nativeBuildDir/native" \
		&& gnuArch="$(uname -m)" \
		&& ./configure \
			--build="$gnuArch" \
			--libdir="$TOMCAT_NATIVE_LIBDIR" \
			--prefix="$CATALINA_HOME" \
			--with-apr="$(which apr-1-config)" \
			--with-java-home="$(docker-java-home)" \
			--with-ssl=yes \
		&& make -j$(getconf _NPROCESSORS_ONLN) \
		&& make install \
	) \
	&& rm -rf "$nativeBuildDir" \
	&& rm bin/tomcat-native.tar.gz

# verify Tomcat Native is working properly
RUN set -e \
    && unset CATALINA_HOME \
	&& nativeLines="$(catalina.sh configtest 2>&1)" \
	&& nativeLines="$(echo "$nativeLines" | grep 'Apache Tomcat Native')" \
	&& nativeLines="$(echo "$nativeLines" | sort -u)" \
	&& if ! echo "$nativeLines" | grep 'INFO: Loaded APR based Apache Tomcat Native library' >&2; then \
		echo >&2 "$nativeLines"; \
		exit 1; \
	fi

EXPOSE 8080
CMD ["catalina.sh", "run"]
