# FFMPEG insert into base Alpine minimize image size

FROM 		sdurrheimer/alpine-glibc:latest
MAINTAINER 	Nachochip <blockchaincolony@gmail.com>

ADD 	ffmpeg.tar.gz	/usr/local/
ADD 	libc.conf 	/etc/ld.so.conf.d/


CMD           ["--help"]
ENTRYPOINT    ["ffmpeg"]
