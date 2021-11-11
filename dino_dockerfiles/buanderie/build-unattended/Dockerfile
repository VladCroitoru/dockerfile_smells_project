FROM ubuntu:zesty

RUN apt-get update && apt-get -y upgrade

# Install the following utilities (required by poky)
RUN apt-get install -y build-essential chrpath curl diffstat gcc-multilib gawk git libsdl1.2-dev texinfo unzip wget xterm dos2unix git mkisofs syslinux-utils syslinux qt5-default qtmultimedia5-dev libqt5multimediawidgets5 libqt5multimedia5-plugins libqt5multimedia5 net-tools git build-essential cmake libnl-3-dev libnl-genl-3-dev libnl-nf-3-dev libssl-dev libpcap-dev gstreamer1.0-plugins-bad gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly libgstrtspserver-1.0-de

# Additional host packages required by poky/scripts/wic
# RUN apt-get install -y bzip2 dosfstools mtools parted syslinux tree

# Add "repo" tool (used by many Yocto-based projects)
# RUN curl http://storage.googleapis.com/git-repo-downloads/repo > /usr/local/bin/repo
# RUN chmod a+x /usr/local/bin/repo

# Create user "jenkins"
RUN id jenkins 2>/dev/null || useradd --uid 1000 --create-home jenkins

# Create a non-root user that will perform the actual build
RUN id build 2>/dev/null || useradd --uid 30000 --create-home build
RUN echo "build ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers

USER build
WORKDIR /home/build
CMD "/bin/bash"

# EOF
