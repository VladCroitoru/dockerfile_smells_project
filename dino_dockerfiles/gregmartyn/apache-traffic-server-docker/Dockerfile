FROM fedora:24

# default is 'dumb'. that cripples less, vim, coloring, etc
ENV TERM xterm-256color

WORKDIR /tmp

# putting && on next line, because then it's more obvious that
# the new line is a separate command
RUN dnf -y upgrade \
	&& dnf clean packages

# https://cwiki.apache.org/confluence/display/TS/Fedora
# build dependencies
RUN dnf -y install make pkgconfig gcc-c++ openssl-devel tcl-devel expat-devel pcre-devel perl-ExtUtils-MakeMaker \
		libcap libcap-devel hwloc hwloc-devel ncurses-devel libcurl-devel \
		libunwind libunwind-devel \
		git autoconf automake libtool \
	&& dnf clean packages

WORKDIR /usr/local/src

RUN git clone https://git-wip-us.apache.org/repos/asf/trafficserver.git

WORKDIR /usr/local/src/trafficserver

RUN git checkout master

RUN autoreconf -if \
	&& ./configure --enable-experimental-plugins \
	&& make -j4 \
	&& make check \
	&& make install \
	&& make distclean

WORKDIR /usr/local/bin

# make it easier to find the config for anyone running a shell inside the container
RUN ln -s /usr/local/etc/trafficserver /etc/trafficserver
RUN ln -s /usr/local/bin/trafficserver /etc/init.d/trafficserver
RUN ln -s /usr/local/var/log/trafficserver /var/log/trafficserver


# TODO: export the /usr/local folder to a pristine image
# TODO: just export the etc folder as a volume with docs for how to cp the defaults out of the container

# records.config

# enable http2
RUN sed -i 's/CONFIG proxy.config.http2.enabled INT 0/CONFIG proxy.config.http2.enabled INT 1/g' /etc/trafficserver/records.config

# listen on port 80 and 443 for http 1 & 2 and ipv4 & ipv6
RUN sed -i 's/CONFIG proxy.config.http.server_ports STRING 8080/CONFIG proxy.config.http.server_ports STRING 80:proto=http2;http 80:ipv6:proto=http2;http 443:proto=http2;http:ssl 443:ipv6:proto=http2;http:ssl/g' /etc/trafficserver/records.config


# lets client push data into cache
#RUN sed -i 's/CONFIG proxy.config.http.push_method_enabled INT 0/CONFIG proxy.config.http.push_method_enabled INT 1/g' /etc/trafficserver/records.config

# client can't bypass cache if 1 (more secure, but harder to debug)
#RUN sed -i 's/CONFIG proxy.config.http.cache.ignore_client_cc_max_age INT 1/CONFIG proxy.config.http.cache.ignore_client_cc_max_age INT 0/g' /etc/trafficserver/records.config

# trafficserver is hardcoded to use /etc/resolv.conf unless specified here
# CONFIG proxy.config.dns.resolv_conf STRING etc/trafficserver/resolv.conf

# set proxy.config.proxy_name?

# https://docs.trafficserver.apache.org/records.config#proxy-config-url-remap-pristine-host-hdr
# turn it on if the backend should see the original host header


# remap.config

#map http://www.example.com:8080/ http://www.example.com/
#reverse_map http://www.example.com/ http://www.example.com:8080/

#map http://ats.example.com:8080/myCI/ http://{cache} @action=allow @src_ip=127.0.0.1




# storage.config

# increase the cache size from 256M => 5G
RUN sed -i 's#var/trafficserver 256M#var/trafficserver 5G#g' /etc/trafficserver/storage.config

VOLUME ["/usr/local/etc/trafficserver", "/usr/local/var/log/trafficserver"]

EXPOSE 80 443

ENTRYPOINT ["/usr/local/bin/traffic_cop"]
