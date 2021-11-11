# Build:
#  docker build -t gbevan/vagrant-meanio .
#
# Example Vagrantfile:
#   VAGRANTFILE_API_VERSION = "2"
#   Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
#     config.vm.define "slm.io", primary: true do |slmio|
#       slmio.vm.provision "shell", inline: '/usr/bin/mongod --config /etc/mongod.conf --fork'
#       slmio.vm.synced_folder "src/", "/home/vagrant/appserver/packages/custom"
#       slmio.vm.provider "docker" do |d|
#         d.image = "gbevan/vagrant-meanio:latest"
#         d.has_ssh = true
#       end
#     end
#   end
#
# Run:
#  vagrant up --provider=docker
#
# resolve dns issues:
# /etc/conf/docker
#  DOCKER_OPTS="--dns ip_1 --dns ip_2"
#

FROM ubuntu:latest
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C
ENV LC_ALL=C

# Dependencies + Vagrant
RUN \
    apt-get -yq update && \
    apt-get dist-upgrade -yq && \
    apt-get install -yqq wget aptitude htop vim vim-puppet git traceroute dnsutils \
      curl ssh sudo psmisc gcc make build-essential libfreetype6 libfontconfig augeas-tools && \
    mkdir /var/run/sshd && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config && \
    useradd --create-home -s /bin/bash vagrant && \
    mkdir -p /home/vagrant/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys && \
    chown -R vagrant: /home/vagrant/.ssh && \
    echo -n 'vagrant:vagrant' | chpasswd && \
    touch /home/vagrant/.hushlogin && \
    mkdir -p /etc/sudoers.d && \
    echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant && \
    chmod 0440 /etc/sudoers.d/vagrant && \
    echo "set modeline" > /etc/vim/vimrc.local && \
    echo "export TERM=vt100\nexport LANG=C\nexport LC_ALL=C" > /etc/profile.d/dockenv.sh && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Mongodb & mean-cli
RUN \
    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/mongodb.list && \
    apt-get -yq update && \
    apt-get install -yqq mongodb-org && \
    curl -sL https://deb.nodesource.com/setup | sudo bash - && \
    apt-get -yq update && \
    apt-get install -yqq nodejs && \
    apt-get clean && \
    npm install -g grunt-cli && \
    npm install -g gulp && \
    npm install -g karma-cli && \
    npm install -g mocha && \
    npm install -g bower && \
    npm install -g mean-cli && \
    npm cache clean && \
    rm -rf /var/lib/mongodb/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

# App init
RUN \
    /usr/bin/mongod --config /etc/mongod.conf --fork && \
    su - vagrant -c'echo -e "\n\n \n" | mean init appserver && cd appserver && npm install && mean install mean-admin && npm cache clean; bower cache clean' && \
    perl -e 'local $/=undef; open(GR,"</home/vagrant/appserver/Gruntfile.js"); binmode GR; $F=<GR>; $F=~s/(mochaTest: {.\s*options: {)/$1\n        timeout: 20000,/ms; open(NG, ">/home/vagrant/appserver/Gruntfile.js"); print NG $F' && \
    su - vagrant -c'cd appserver && grunt test' && \
    killall mongod && \
    rm -rf /var/lib/mongodb/* /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/sbin/sshd", "-D", "-e"]
EXPOSE 22 3000
