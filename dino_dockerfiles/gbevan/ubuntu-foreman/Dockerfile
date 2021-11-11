# Build:
#   docker build -t gbevan/ubuntu-foreman .
#
# Run:
#  docker run --restart=always -d \
#    -p 443:443 -p 8443:8443 -p 8140:8140 \
#    -h foreman.example.com \
#    --init \
#    --name foreman \
#    gbevan/ubuntu-foreman
#
# tail log:
#   docker ps | awk '/gbevan\/ubuntu-foreman/ {print $1}' | xargs docker logs -f
#
# Point your browser at https://your-host
#
# resolve dns issues:
# /etc/conf/docker
#  DOCKER_OPTS="--dns ip_1 --dns ip_2"
#
# Used the following projects as reference:
#   riskable/docker-foreman
#   xnaveira/foreman-docker

FROM ubuntu:16.04
MAINTAINER Graham Bevan "graham.bevan@ntlworld.com"

ENV FOREMANVER 1.15
ENV DEBIAN_FRONTEND noninteractive
ENV FOREOPTS --foreman-locations-enabled=true \
        --enable-foreman-compute-ec2 \
        --enable-foreman-compute-gce \
        --enable-foreman-compute-ovirt \
        --enable-foreman-compute-vmware \
        --enable-foreman-compute-libvirt \
        --enable-foreman-compute-openstack \
        --enable-foreman-compute-rackspace \
        --enable-puppet \
        --puppet-listen=true \
        --puppet-show-diff=true \
        --puppet-server-envs-dir=/etc/puppet/environments \
        --foreman-proxy-dhcp-option-domain='' \
        --foreman-proxy-dns-zone='' \
        --puppet-srv-domain=''
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/puppetlabs/bin:/sbin:/bin

COPY start-image.sh /

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install ca-certificates wget && \
    wget https://apt.puppetlabs.com/puppetlabs-release-pc1-xenial.deb && \
    dpkg -i puppetlabs-release-pc1-xenial.deb && \
    apt-get update && \
    apt-get install -y wget aptitude htop vim vim-puppet git traceroute dnsutils && \
    echo "deb http://deb.theforeman.org/ xenial $FOREMANVER" > /etc/apt/sources.list.d/foreman.list && \
    echo "deb http://deb.theforeman.org/ plugins $FOREMANVER" >> /etc/apt/sources.list.d/foreman.list && \
    wget -q http://deb.theforeman.org/pubkey.gpg -O- | apt-key add - && \
    apt-get install -y software-properties-common && \
    apt-add-repository ppa:git-core/ppa -y && \
    apt-get update && \
    apt-get install -y foreman-installer && \
    apt-get install -y git python-pip iotop sysstat krb5-user libkrb5-dev python-dev python-jinja2 python-yaml python-paramiko python-httplib2 python-six python-crypto sshpass && \
    apt-add-repository -y ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible && \
    apt-get purge -y python-requests python-requests-whl && \
    apt-get autoremove -y && \
    apt-get install -y libffi-dev libssl-dev locales && \
    /usr/bin/pip install --upgrade --ignore-installed pip setuptools urllib3 && \
    /usr/bin/pip install cryptography==2.0.3 && \
    /usr/bin/pip install netaddr && \
    /usr/bin/pip install 'pywinrm>=0.1.1' && \
    /usr/bin/pip install kerberos==1.2.2 && \
    /usr/bin/pip install requests_kerberos && \
    /usr/bin/pip install pyvmomi==6.0.0.2016.6 && \
    echo "set modeline" > /root/.vimrc && \
    echo "export TERM=vt100" >> /root/.bashrc && \
    LANG=en_US.UTF-8 locale-gen --purge en_US.UTF-8 && \
    echo 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale && \
    (dpkg-reconfigure --frontend=noninteractive locales || /bin/true) && \
    rm -f /usr/share/foreman-installer/checks/hostname.rb && \
    export FACTER_fqdn="foreman.example.com" && \
    echo "127.1.1.2  foreman.example.com" >> /etc/hosts && \
    echo "Running foreman installer" && \
    (/usr/sbin/foreman-installer $FOREOPTS || /bin/true) && \
    sed -i -e "s/START=no/START=yes/g" /etc/default/foreman && \
    chmod 700 /start-image.sh && \
    /etc/init.d/puppetserver stop && \
    export PATH=$PATH:/opt/puppetlabs/bin && \
    sed -i 's?:/usr/bin:?:/usr/bin:/opt/puppetlabs/bin:?' /etc/environment && \
    /opt/puppetlabs/bin/puppet resource service puppet ensure=stopped && \
    /opt/puppetlabs/bin/puppet resource service apache2 ensure=stopped && \
    export SSLDIR=`puppet config print ssldir --section master` && \
    rm -rf $SSLDIR && \
    touch /var/lib/foreman/.firsttime

EXPOSE 443
EXPOSE 8140
EXPOSE 8443

# all future startups
ENTRYPOINT /start-image.sh
