FROM base
#version 2
env   DEBIAN_FRONTEND noninteractive

# REPOS
run    apt-get install -y software-properties-common
run    add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc) universe"
run    apt-get --yes update
run    apt-get --yes upgrade --force-yes

# TOOLS
run    apt-get install -y -q curl git wget 

env   DEBIAN_FRONTEND dialog

## App required
run    apt-get --yes install redis-server --force-yes
run    apt-get --yes install supervisor python-pip libavcodec-extra-53 ffmpeg --force-yes

## Setup App
add    . /opt
run    cd /opt/app ; python setup.py install; mkdir data

add    ./supervisor/supervisord.conf /etc/supervisor/supervisord.conf
add    ./supervisor/conf.d/yodl.conf /etc/supervisor/conf.d/yodl.conf

expose 8888

CMD ["/usr/bin/supervisord"]
