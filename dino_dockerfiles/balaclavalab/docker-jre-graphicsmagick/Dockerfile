FROM openjdk:16
RUN mkdir -p mkdir -p /etc/yum/vars \
  && touch /etc/yum/vars/ociregion \
  && touch /etc/dnf/dnf.conf \
  && microdnf install dnf -y \
  && dnf install -y --nogpgcheck \
           https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm \
	   https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm \
           https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm \
  && dnf install -y http://mirror.centos.org/centos/8/PowerTools/x86_64/os/Packages/SDL2-2.0.10-2.el8.x86_64.rpm \
  && dnf install -y GraphicsMagick ffmpeg
