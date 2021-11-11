FROM node

# vagrant
RUN apt-get update \
&&  env DEBIAN_FRONTEND=noninteractive apt-get install -y qemu-kvm libvirt-bin ebtables dnsmasq libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev rsync nfs-kernel-server \
&&  apt-get clean \
&&  usermod -a -G libvirt-qemu root

RUN curl -O https://releases.hashicorp.com/vagrant/1.9.1/vagrant_1.9.1_x86_64.deb \
&&  dpkg -i vagrant_1.9.1_x86_64.deb \
&&  rm vagrant_1.9.1_x86_64.deb \
&&  vagrant plugin install vagrant-libvirt

# web app
ENV VER=${VER:-master} \
    REPO=https://github.com/dorissschoi/vagrantvm \
    APP=/usr/src/app

RUN git clone -b $VER $REPO $APP

WORKDIR $APP

RUN npm install \
&&  node_modules/.bin/bower install --allow-root

EXPOSE 1337                                                                     
                                                                                
ENTRYPOINT ./entrypoint.sh
