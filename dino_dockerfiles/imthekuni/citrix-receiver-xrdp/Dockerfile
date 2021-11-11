FROM phusion/baseimage:0.9.16
ENV DEBIAN_FRONTEND noninteractive
# Set correct environment variables
ENV HOME /root
ENV TERM xterm
# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Add local files
ADD src/ /root/

# set workdir
WORKDIR /

# Expose ports
EXPOSE 6080
EXPOSE 5900
EXPOSE 3389

# set startup file
RUN mv /root/firstrun.sh /etc/my_init.d/firstrun.sh && \
chmod +x /etc/my_init.d/firstrun.sh && \

# update apt and install dependencies
mv /root/excludes /etc/dpkg/dpkg.cfg.d/excludes && \
apt-get update && \
apt-get install -y --force-yes --no-install-recommends wget openjdk-7-jre supervisor sudo nano net-tools lxde x11vnc xvfb gtk2-engines-murrine ttf-ubuntu-font-family firefox lxterminal && \
apt-get install -y xrdp libreoffice && \

# create ubuntu user
useradd --create-home --shell /bin/bash --user-group --groups adm,sudo ubuntu && \
echo "ubuntu:PASSWD" | chpasswd && \

# set user ubuntu to same uid and guid as nobody:users in unraid
usermod -u 99 ubuntu && \
usermod -g 100 ubuntu && \


# swap in modified xrdp.ini
mv /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.original && \
mv /root/xrdp.ini /etc/xrdp/xrdp.ini && \
chown root:root /etc/xrdp/xrdp.ini && \

# Install via mark911 instructions
#dpkg --add-architecture i386 && \
apt-get update && \

apt-get install -f -y firefox && \
apt-get install -f -y chromium-browser && \
apt-get install -f -y xdg-utils && \

#apt-get install -f -y libwebkit-1.0-2:i386 && \
#apt-get install -f -y libwebkitgtk-1.0-0 && \
#dpkg -i /root/icaclient_*.deb && \

#apt-get -f install && \

#ln -s /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts/ && \
#c_rehash /opt/Citrix/ICAClient/keystore/cacerts/ && \

#rm -f /usr/lib/mozilla/plugins/npwrapper.npica.so /usr/lib/firefox/plugins/npwrapper.npica.so && \
#rm -f /usr/lib/mozilla/plugins/npica.so && \
#ln -s /opt/Citrix/ICAClient/npica.so /usr/lib/mozilla/plugins/npica.so && \
#ln -s /opt/Citrix/ICAClient/npica.so /usr/lib/firefox-addons/plugins/npica.so && \

#xdg-mime default wfica.desktop application/x-ica && \

# clean up
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
/usr/share/man /usr/share/groff /usr/share/info \
/usr/share/lintian /usr/share/linda /var/cache/man && \
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
(( find /usr/share/doc -empty|xargs rmdir || true ))
