FROM	debian:latest AS build
MAINTAINER	lufia <lufia@lufia.org>

ENV	PLAN9=/usr/local/plan9 \
	PATH=$PATH:/usr/local/plan9/bin

ADD	*.c mkfile /app/
RUN	apt-get update && \
	apt-get install -y gcc git
RUN	mkdir -p $PLAN9 && \
	cd $PLAN9 && \
	git clone https://github.com/9fans/plan9port . && \
	./INSTALL && \
	cd /app && \
	mk install clean && \
	cd $PLAN9 && \
	rm -rf \
		.git .gitignore \
		CHANGES CONTRIBUTING.md CONTRIBUTORS \
		dist face font lib lp \
		mac mail man news \
		postscript proto \
		src tmac troff unix

FROM	debian:latest
ENV	PLAN9=/usr/local/plan9 \
	PATH=$PATH:/usr/local/plan9/bin \
	VENTI_SIZE=10G

COPY	--from=build $PLAN9 $PLAN9
ADD	venti.conf startup /app/
RUN	chmod +x /app/startup
VOLUME	["/mnt/venti"]
EXPOSE	80 17034
WORKDIR	/mnt/venti

CMD	["/app/startup"]
