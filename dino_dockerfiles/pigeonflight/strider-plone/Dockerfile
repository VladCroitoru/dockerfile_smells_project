# DOCKER-VERSION 0.7.6

from  ubuntu
maintainer David Bain <david@alteroo.com>

# based on niallo/strider by Niall O'Higgins <niallo@frozenridge.co>
# do this as single-line run until https://github.com/dotcloud/docker/issues/1171 is fixed
run  \
    echo "PATH=$PATH:/src/appengine" ;\
    useradd -m strider ;\
    CUSTOM_PACKAGES="libxslt-dev libjpeg8-dev poppler-utils language-pack-en-base python-virtualenv python-lxml python-imaging tmux wv libgeos-c1 libpcre3-dev pkg-config libncurses-dev autotools-dev automake1.9 libtool autoconf phantomjs ";\
    dpkg-divert --local --rename --add /sbin/initctl ;\
    ln -s /bin/true /sbin/initctl ;\
    echo "deb http://archive.ubuntu.com/ubuntu quantal main universe" > /etc/apt/sources.list ;\
    echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' > /etc/apt/sources.list.d/10gen.list ;\
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 ;\
    apt-get update ;\
    apt-get install -y curl wget supervisor openssh-server make build-essential libssl-dev python python-dev git default-jre-headless mongodb-10gen ;\
    apt-get install -y $CUSTOM_PACKAGES ;\
    locale-gen en_US en_US.UTF-8 ;\
    mkdir -p /var/run/sshd ;\
    mkdir -p /var/log/supervisor ;\
    mkdir -p /data/db ;\
    locale-gen en_US en_US.UTF-8 ;\
    curl https://raw.github.com/isaacs/nave/master/nave.sh > /bin/nave && chmod a+x /bin/nave ;\
    nave usemain stable ;\
    echo 'root:str!der' | chpasswd ;\
    git clone -b master https://github.com/Strider-CD/strider.git /src ;\
    cd /src; (rm -rf node_modules || exit 0) && npm install ;\
    /usr/bin/mongod --smallfiles --fork --logpath mongo.log ;\
    sleep 2 ;\
    /src/bin/strider addUser --email test@example.com --password dontlook --admin true ;\
    /usr/bin/mongod --shutdown ;\
    /usr/bin/mongod --smallfiles --fork --logpath mongo.log ;\
    sleep 2 ;\
    echo "db.users.find()" | mongo localhost/strider-foss | grep test@example.com ;\
    chown -R strider /src ;\

#inject appengine files
add docker/appengine /src/appengine
add docker/etc/bash /etc/

# inject supervisord.conf
add  docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# supervisord will run ssh, and strider, and restart them if they crash
cmd  ["/usr/bin/supervisord", "-n"]

# 22 is ssh server
# 3000 is strider
# You can find out what ports they are mapped to on your host by running `docker ps`
expose 22 3000

