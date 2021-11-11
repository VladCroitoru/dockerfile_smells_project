#
# 1science Alpine Linux image
#

FROM alpine:3.5
MAINTAINER 1science Devops Team <devops@1science.org>

# Install root filesystem
ADD ./rootfs /

# Install base packages
RUN apk update && apk upgrade && \
    apk add curl wget bash tree && \
    echo -ne "Alpine Linux 3.5 image. (`uname -rsv`)\n" >> /root/.built

# Define bash as default command
CMD ["/bin/bash"]
