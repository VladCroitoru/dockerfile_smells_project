FROM alpine:3.5

ARG ALPINE_MIRROR=http://mirrors.aliyun.com/alpine
ARG NPC_DL_MIRROR=http://npc.nos-eastchina1.126.net/dl

RUN echo -e "$ALPINE_MIRROR/v3.5/main\n$ALPINE_MIRROR/v3.5/community" >/etc/apk/repositories \
	&& npc_dl_add(){ wget "$NPC_DL_MIRROR/$1" && tar -zx -C /usr/bin -f "$1" && rm -f "$1"; } \
	&& npc_dl_add dumb-init_1.2.0_amd64.tar.gz \
	&& npc_dl_add jq_1.5_linux_amd64.tar.gz \
	&& npc_dl_add json2hcl_v0.0.6_linux_amd64.tar.gz \
	&& npc_dl_add consul_0.7.5_linux_amd64.tar.gz \
	&& apk add --no-cache bash curl openssh-client git

ADD scripts /
RUN chmod a+x /*.sh
CMD ["/launch.sh"]