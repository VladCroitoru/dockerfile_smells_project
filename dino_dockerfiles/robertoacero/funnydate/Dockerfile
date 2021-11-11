FROM library/debian:wheezy

MAINTAINER roberto.acero

RUN	apt-get update \ 
	&& apt-get -y install funny-manpages manpages man-db \
	&& apropos date

ENTRYPOINT [ "man" ]

CMD [ "1fun" ]
