FROM scratch

LABEL 	maintainer="khirin" \
	name="Alpine Base Image" \
	version="3.5" \
	date="20170315" \
	image_version="1.6"

ENV 	LC_ALL="C.UTF-8" \
        LANG="fr_FR.UTF-8" \
        LANGUAGE="fr_FR.UTF-8" \
	TZ="Europe/Paris"

ARG	ROOT_PWD="saFKJij3eLACw"

ADD ["sources/rootfs.tar.gz", "/"]

# Timezone & Busybox Configuration
RUN 	apk --update add tzdata busybox-suid \
	&& echo "${TZ}" > /etc/timezone \
	&& (cd /usr/share/zoneinfo; rm -rf right America Asia Pacific Africa US Australia Atlantic Antarctica Indian Canada Brazil) \
	&& rm -rf /var/cache/apk/* \
# Root pwd
	&& echo "root:${ROOT_PWD}" | chpasswd -e
