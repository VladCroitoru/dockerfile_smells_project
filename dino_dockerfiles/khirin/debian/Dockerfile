FROM scratch

LABEL	maintainer="khirin" \
	name="Debian Base Image" \
	version="8" \
	date="20170506" \
	image_version="1.1"
	
ENV     LC_ALL="C.UTF-8" \
        LANG="fr_FR.UTF-8" \
        LANGUAGE="fr_FR.UTF-8" \
        TZ="Europe/Paris"

ARG     ROOT_PWD="saFKJij3eLACw"

ADD sources/rootfs.tar.xz /

RUN apt-get update \
	&& apt-get install tzdata \
	&& echo "${TZ}" > /etc/timezone \
	&& dpkg-reconfigure -f noninteractive tzdata \
	&& (cd /usr/share/zoneinfo; rm -rf right America Asia Pacific Africa US Australia Atlantic Antarctica Indian Canada Brazil) \
	&& apt-get clean \
# Root pwd
        && echo "root:${ROOT_PWD}" | chpasswd -e
