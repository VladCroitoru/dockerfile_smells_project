FROM ubuntu:xenial
MAINTAINER Markos Chandras <mchandras@suse.de>

# Install dependencies
RUN apt-get update && apt-get install -y -q=3 yum yum-utils rpm zypper kpartx python-pip debootstrap gnupg2 curl sudo apt-utils qemu-utils git e2fsprogs

# Make sure sudo group can do everything
RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Add user
RUN useradd -m builder && echo "builder:builder" | chpasswd && gpasswd -a builder sudo

# Make user the default one
USER builder

# Add build script
ADD do-build.sh /usr/bin
