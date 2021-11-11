FROM node:boron
MAINTAINER Josh Cox <josh 'at' webhosting.coop>

ENV MEANSHOP_UPDATED 20170318
ENV LANG en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive \
apt-get -qq update && apt-get -qqy dist-upgrade && \
apt-get -qqy --no-install-recommends install \
build-essential perl ruby rake locales \
procps ca-certificates wget pwgen curl sudo && \
echo 'en_US.ISO-8859-15 ISO-8859-15'>>/etc/locale.gen && \
echo 'en_US ISO-8859-1'>>/etc/locale.gen && \
echo 'en_US.UTF-8 UTF-8'>>/etc/locale.gen && \
locale-gen && \
useradd meanshop && \
gpasswd -a meanshop sudo && \
echo '%sudo ALL=(ALL) NOPASSWD:ALL'>> /etc/sudoers && \
apt-get -y autoremove && \
apt-get clean && \
rm -Rf /var/lib/apt/lists/* && \
cd / && \
git clone https://github.com/Thalhalla/meanshop.git && \
mkdir -p /meanshop/client/bower_components && \
chown -R meanshop. /meanshop && \
mkdir -p /home/meanshop && \
chown -R meanshop. /home/meanshop

USER meanshop
WORKDIR /meanshop

ENV RUBY_TARGET ruby-2.3.3
# Install app dependencies
RUN bash -l -c "curl -sSL https://get.rvm.io | bash -s stable && \
source /home/meanshop/.rvm/scripts/rvm && \
rvm requirements && \
rvm install --binary $RUBY_TARGET && \
rvm use --default $RUBY_TARGET && \
source /home/meanshop/.rvm/scripts/rvm && \
gem install sass && \
sudo npm install -g bower grunt-cli yo gulp"

USER root
RUN chown -R meanshop. /meanshop \
&& SUDO_FORCE_REMOVE=yes apt-get remove -qqy sudo
USER meanshop
CMD ["npm", "start"]
