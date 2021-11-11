from centos:7
maintainer ulrich.schreiner@gmail.com

add nginx.repo /etc/yum.repos.d/nginx.repo
run yum -y install createrepo git nginx git-daemon
volume /data
run mkdir /src
add makerepo.sh /src/makerepo.sh
add updaterepo.sh /src/updaterepo.sh
add startup.sh /src/startup.sh
add repo /src/layout
add repository.conf /etc/nginx/conf.d/repository.conf
run rm /etc/nginx/conf.d/default.conf
expose 9418
expose 80
cmd /src/startup.sh
