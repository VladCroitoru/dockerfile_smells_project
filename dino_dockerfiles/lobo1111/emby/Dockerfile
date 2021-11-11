from centos:7

run yum install -y wget epel-release
run cd /etc/yum.repos.d/; wget http://download.opensuse.org/repositories/home:emby/CentOS_7/home:emby.repo
run yum install -y emby-server

volume /var/lib/emby-server

entrypoint emby-server start
