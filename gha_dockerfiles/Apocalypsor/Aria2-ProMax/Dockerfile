FROM p3terx/aria2-pro

COPY rootfs /
COPY aria2_ban_thunder /Aria2-Ban

RUN apk add --no-cache --update nodejs ipset git npm iptables \
    && cd /Aria2-Ban && npm install /Aria2-Ban 
