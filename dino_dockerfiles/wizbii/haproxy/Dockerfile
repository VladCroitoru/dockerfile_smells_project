FROM debian:jessie

# Lua
RUN LUA_VERSION=5.3.3 \
    buildDeps="libc6-dev libreadline-dev gcc curl make" \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
    && curl -L http://www.lua.org/ftp/lua-${LUA_VERSION}.tar.gz | tar xzf - \
    && cd /lua-$LUA_VERSION \
    && make linux test \
    && make install \
    && cd .. && rm /lua-$LUA_VERSION -rf \\
    && apt-get purge -y --auto-remove $buildDeps


# Ucarp
ENV UCARP_INTERFACE=lo \
    UCARP_SOURCEADDRESS=127.0.0.1 \
    UCARP_SOURCEPREFIX=8 \
    UCARP_VIRTUALADDRESS=127.0.0.1 \
    UCARP_VIRTUALPREFIX=8 \
    UCARP_VIRTUALGATEWAY=127.0.0.1 \
    UCARP_VHID=255 \
    UCARP_PASS=password \
    UCARP_UPSCRIPT=/etc/ucarp/vip-up.sh \
    UCARP_DOWNSCRIPT=/etc/ucarp/vip-down.sh

RUN apt-get update && apt-get install -y ucarp netmask iptables \
# from github.com/docker-library/haproxy/blob/master/1.7/Dockerfile
    && apt-get install -y libssl1.0.0 libpcre3 --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV HAPROXY_MAJOR 1.7
ENV HAPROXY_VERSION 1.7.1
ENV HAPROXY_MD5 d0acaae02e444039e11892ea31dde478

RUN buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& curl -SL "http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz" -o haproxy.tar.gz \
	&& echo "${HAPROXY_MD5}  haproxy.tar.gz" | md5sum -c \
	&& mkdir -p /usr/src/haproxy \
	&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \
	&& rm haproxy.tar.gz \
	&& make -C /usr/src/haproxy \
		TARGET=linux2628 \
		USE_PCRE=1 PCREDIR= \
		USE_OPENSSL=1 \
		USE_ZLIB=1 \
		USE_LUA=1 \
		LUA_LIB="/usr/local/lib/lua/5.3" \
                LUA_INC="/usr/local/include/lua5.3" \
		all \
		install-bin \
	&& mkdir -p /usr/local/etc/haproxy \
	&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \
	&& rm -rf /usr/src/haproxy \
	&& apt-get purge -y --auto-remove $buildDeps

COPY ucarp-scripts /etc/ucarp
COPY entrypoint.sh /
ENTRYPOINT /entrypoint.sh
