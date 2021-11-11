
FROM phusion/baseimage:master-amd64

ENV DEBIAN_FRONTEND noninteractive
ENV container docker

MAINTAINER FastFreddi

# set random root password
# RUN P="$(dd if=/dev/random bs=1 count=8 2>/dev/null | base64)" ; echo $P && echo "root:$P" | chpasswd
# set to foobar
# RUN P="foobar" ; echo $P && echo "root:$P" | chpasswd

# stuff for HomeSeer
RUN apt-get update && apt-get upgrade -y && \
		apt-get install -y mono-devel mono-vbnc flite chromium-browser aha ffmpeg alsa-base alsa-utils curl sudo wget vim screen && \
 		apt-get -y remove brltty && \
		apt-get update -y && apt-get clean

# HomeSeer Install
RUN wget https://homeseer.com/updates4/linux_4_1_16_0.tar.gz -O homeseer.tar.gz && \
 	tar xvzf homeseer.tar.gz -C /usr/local && rm homeseer.tar.gz

# HomeSeer Startup / Shutdown
ADD runit_run_hs.sh /etc/service/homeseer/run
RUN chmod -R 755 /etc/service/homeseer/run
ADD runit_stop_hs.sh /etc/service/homeseer/control/t
RUN chmod -R 755 /etc/service/homeseer/control/t
ADD hs_stop.sh /usr/local/HomeSeer/hs_stop.sh
RUN chmod -R 755 /usr/local/HomeSeer/hs_stop.sh
ADD shutdown_controller.sh /usr/local/HomeSeer/shutdown_controller.sh
RUN chmod -R 755 /usr/local/HomeSeer/shutdown_controller.sh
ADD upgrade /upgrade
RUN chmod -R 755 /upgrade

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/sbin/my_init"]
