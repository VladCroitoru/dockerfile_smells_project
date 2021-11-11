# Default release is 20.04
ARG BASE_IMAGE_RELEASE=20.04
# Default base image 
ARG BASE_IMAGE=ubuntu

FROM abcdesktopio/oc.nginx:builder as builder

# copy .git for version
COPY .git /.git
# copy data files
COPY var/webModules /var/webModules
# run makefile 
RUN cd /var/webModules && make -B prod 

# --- START Build image ---
FROM $BASE_IMAGE:$BASE_IMAGE_RELEASE

# take care do not set --no-install-recommends   
# lua nginx need install-recommends  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update      && 	                        \
    apt-get install -y   	\
        nginx-extras                                	\
    	sed 			                        \
	lua-any						\
	lua5.1						\	
	lua5.2        					\
	lua5.3						\
    && apt-get clean					\
    && rm -rf /var/lib/apt/lists/*


#
# this is a too log command line 
# but i didn't find a better way to reduce docker image size
# and install kuarocks version 3
#
# install luarocks package 
# luarocks version 3.x deb package does not exist in ubuntu
# luarocks package 
# * lua-resty-jwt
# * lua-resty-string
# * lua-cjson
# * lua-resty-rsa   
# need luarocks version 3.x
# build and install luarocks version 3.x 
# git command is used by luarocks install lua-resty-rsa
#
RUN apt-get update      && 	\
    apt-get install -y  --no-install-recommends 	\
	build-essential			        	\
        git			                        \
	libreadline-dev					\
	wget 						\
	liblua5.1-dev                                   \
        liblua5.2-dev                                   \
        liblua5.3-dev  					\
	zip                                             \
        unzip                                           \
    &&	\
    wget https://luarocks.org/releases/luarocks-3.3.1.tar.gz --no-check-certificate	&& \
    tar zxpf luarocks-3.3.1.tar.gz		     && \
    cd luarocks-3.3.1				     && \
    ./configure 					\
    	--lua-version=5.1  				\
	--prefix=/usr  					\
	--sysconfdir=/etc/luarocks  			\
	--with-lua=/usr  				\
	--with-lua-include=/usr/include/lua5.1  	\
	--with-lua-lib=/usr/local/lib 			\
	--rocks-tree=/usr/local/  			\
    && \		
    make 				&& \
    make install			&& \
    cd ..				&& \
    rm -rf luarocks-3.3.1		&& \
    rm -rf luarocks-3.3.1.tar.gz	&& \
    luarocks install lua-resty-jwt 	&& \
    luarocks install lua-resty-string	&& \
    luarocks install lua-cjson		&& \
    luarocks install lua-resty-rsa      && \
    apt-get remove -y build-essential git libreadline-dev wget &&				\
    apt autoremove -y 			&& \
    apt-get clean			&& \
    rm -rf /var/lib/apt/lists/*

# luarocks is now installed in version 3.3.1

# for debug only
# remove in release
# tools for troubleshooting, but not for prod
RUN DEBIAN_FRONTEND=noninteractive 			\
    apt-get update      &&                              \
    apt-get install -y  --no-install-recommends 	\
	net-tools 	\
	iputils-ping	\
	netcat 		\
	curl		\
	dnsutils        \
	vim		\
    && apt-get clean	\
    && rm -rf /var/lib/apt/lists/*

RUN 	mkdir -p /var/nginx/cache 	&& 	\
	mkdir -p /var/nginx/tmp 	&&	\
	mkdir -p /config 

# COPY generated web site from builder container
COPY --from=builder var/webModules /var/webModules

COPY etc/nginx /etc/nginx
COPY composer /composer
COPY config.payload.default/ /config.payload.default
COPY config.signing.default/ /config.signing.default

EXPOSE 80 443
CMD ["/composer/docker-entrypoint.sh"]
