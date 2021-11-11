FROM alpine:3.6
MAINTAINER Thomas Fanninger <thomas@fanninger.at>

RUN	apk --no-cache --no-progress upgrade -f && \
	apk --no-cache --no-progress add \
	su-exec \
	ca-certificates \
	sqlite \
	bash \
	git \
	linux-pam \
	s6 \
	curl \
	openssh \
	tzdata \
	gitea

ADD	gitea/docker/etc/s6/gitea /etc/s6.d/gitea
ADD	gitea/docker/etc/s6/openssh /etc/s6.d/openssh
ADD	app.ini /etc/templates/app.ini
ADD	setup /etc/s6.d/gitea/setup

RUN	addgroup -S -g 1000 git && \
	adduser -S -H -D -h /data/git -s /bin/bash -u 1000 -G git git && \
	echo "git:$(date +%s | sha256sum | base64 | head -c 32)" | chpasswd && \
	chmod 775 /etc/s6.d/gitea/setup && \
	ln -s /data/gitea/conf/app.ini /var/lib/gitea/conf/app.ini && \
	ln -s /usr/bin/gitea /var/lib/gitea/gitea && \
	sed -i -e 's/\/app\/gitea/\/var\/lib\/gitea/g' /etc/s6.d/gitea/* && \
	ln -s /data/ssh/ssh_host_ed25519_key /etc/ssh/ && \
	ln -s /data/ssh/ssh_host_rsa_key /etc/ssh/ && \
	ln -s /data/ssh/ssh_host_dsa_key /etc/ssh && \
	ln -s /data/ssh/ssh_host_ecdsa_key /etc/ssh/ 

ENV	GITEA_CUSTOM=/data/gitea USER=git
EXPOSE	3000 22
VOLUME	["/data"]
