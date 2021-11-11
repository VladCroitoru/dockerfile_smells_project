FROM alpine:3.8
MAINTAINER firewarm LightingLiu <liuyg@liuyingguang.cn>

# Install root filesystem
ADD ./rootfs /

# Install base packages
RUN apk update && apk add curl bash tree tzdata \
    && cp -r -f /usr/share/zoneinfo/Hongkong /etc/localtime \
    && echo -ne "Alpine Linux 3.8 image. (`uname -rsv`)\n" >> /root/.built
# Define bash as default command
CMD ["/bin/bash"]
