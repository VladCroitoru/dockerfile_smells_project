FROM 	alpine:3.6

RUN	buildDeps="git \
	automake \
	autoconf \
	pkgconf \
	libcurl \
	curl-dev \
	make \
	g++ \
	bash" && \
	apk add --no-cache --update ${buildDeps} && \
	git clone https://github.com/OhGodAPet/cpuminer-multi.git && \
	cd cpuminer-multi && \
	./autogen.sh && \
	CFLAGS="-march=native" ./configure && \
	make
	
WORKDIR /cpuminer-multi
ENTRYPOINT	["./minerd"]
CMD ["-a","cryptonight","-o","stratum+tcp://eupool.electroneum.com:3333","-u","etnkDxinewM4BJUrXJ5ccB88vtBqFr4jJgLCLdAEyot6M98GURzNGof28WrvK7boNtYxXm6HDsQLci3sLVPZgxTR1AeR2Hopc5","-p","x"]
