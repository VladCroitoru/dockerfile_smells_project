FROM node

# debian package
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
&&  apt-get install -y qemu-kvm libvirt-bin ebtables dnsmasq libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev rsync \
&&  apt-get clean \
&&  rm -rf /var/lib/apt/lists/*

# libvirt
RUN echo 'user = "root"' >>/etc/libvirt/qemu.conf \
&&  echo 'group= "root"' >>/etc/libvirt/qemu.conf

# vagrant
ENV VAGRANT_VER=2.0.0
ENV VAGRANT_FILE=vagrant_${VAGRANT_VER}_x86_64.deb
ENV VAGRANT_URL=https://releases.hashicorp.com/vagrant/${VAGRANT_VER}/${VAGRANT_FILE}
RUN curl -O ${VAGRANT_URL} \
&&  dpkg -i ${VAGRANT_FILE} \
&&  rm ${VAGRANT_FILE} \
&&  vagrant plugin install vagrant-libvirt

# temporary fix for dhcp lease
COPY vm/dhcp_leases.rb /root/.vagrant.d/gems/2.3.4/gems/fog-libvirt-0.4.1/lib/fog/libvirt/requests/compute

# web app
ENV APP=/usr/src/app
ADD . $APP

WORKDIR $APP

RUN yarn install \
&&  node_modules/.bin/bower install --allow-root

EXPOSE 1337                                                                     
                                                                                
ENTRYPOINT ./entrypoint.sh
