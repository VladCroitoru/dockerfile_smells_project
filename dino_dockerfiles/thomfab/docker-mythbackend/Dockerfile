FROM phusion/baseimage:0.9.22
# updated from an0t8/mythtv-server

# Set correct environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV HOME="/root"
ENV TERM=xterm
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# These should be set at runtime.
ENV USER_ID=99
ENV GROUP_ID=100
ENV DATABASE_HOST=mysql
ENV DATABASE_PORT=3306
ENV DATABASE_ROOT=root
ENV DATABASE_ROOT_PWD=pwd

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Expose ports
EXPOSE 3389 5000/udp 6543 6544


# set volumes
VOLUME /home/mythtv /var/lib/mythtv/db_backups /mnt/recordings /mnt/video

# Add files
COPY files /root/

# chfn workaround - Known issue within Dockers
RUN ln -s -f /bin/true /usr/bin/chfn && \

# Set the locale
locale-gen en_US.UTF-8 && \


mkdir -p /etc/my_init.d && \
mv /root/startup/* /etc/my_init.d && \
rmdir /root/startup && \
chmod +x /etc/my_init.d/* && \

# add repos
apt-add-repository ppa:ubuntu-mate-dev/ppa && \
apt-add-repository ppa:ubuntu-mate-dev/xenial-mate && \


# install mate and dependencies
apt-get update -qq && \
apt-get install -qy --force-yes --no-install-recommends \
wget \
sudo \
mate-desktop-environment-core \
x11vnc \
xvfb \
gtk2-engines-murrine \
ttf-ubuntu-font-family \
supervisor && \

# install xrdp
apt-get install \
xrdp -y && \
mv /root/xrdp.ini /etc/xrdp/xrdp.ini && \

# add repositories
add-apt-repository universe -y && \
apt-add-repository ppa:mythbuntu/0.29 -y && \
apt-get update -qq && \

# install mythtv-backend, database and ping util
apt-get install -y --no-install-recommends mythtv-backend mythtv-database xmltv unzip mythtv-status iputils-ping && \

# install mythweb
apt-get install \
mythweb -y && \

# install mythnuv2mkv
apt-get install \
libmyth-python mythtv-transcode-utils perl mplayer mencoder wget imagemagick \
libmp3lame0 x264 faac faad mkvtoolnix vorbis-tools gpac -y && \

mv /root/mythnuv2mkv.sh /usr/bin/ && \
chmod +x /usr/bin/mythnuv2mkv.sh && \

# install hdhomerun utilities
apt-get install \
hdhomerun-config-gui \
hdhomerun-config -y && \

# set mythtv to uid and gid
usermod -u ${USER_ID} mythtv && \
usermod -g ${GROUP_ID} mythtv && \

# create/place required files/folders
mkdir -p /home/mythtv/.mythtv /var/lib/mythtv /var/log/mythtv /root/.mythtv /mnt/recordings /mnt/video && \

# set a password for user mythtv and add to required groups
echo "mythtv:mythtv" | chpasswd && \
usermod -s /bin/bash -d /home/mythtv -a -G users,mythtv,adm,sudo mythtv && \

# set permissions for files/folders
chown -R mythtv:users /var/lib/mythtv /var/log/mythtv && \
chown mythtv:users /mnt/recordings /mnt/video && \

# set up passwordless sudo
echo '%adm ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/adm && \
chmod 0440 /etc/sudoers.d/adm && \

# clean up
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
/usr/share/man /usr/share/groff /usr/share/info \
/usr/share/lintian /usr/share/linda /var/cache/man && \
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
(( find /usr/share/doc -empty|xargs rmdir || true ))
