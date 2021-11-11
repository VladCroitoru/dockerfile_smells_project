ARG BASE_TAG=latest
FROM apluslms/grading-base:$BASE_TAG

ARG NODE_VERSION=11

RUN apt_install apt-transport-https \
 && curl -sSL https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - >/dev/null \
 && codename=$(cat /etc/os-release|grep '^VERSION='|cut '-d(' -f2|cut '-d)' -f1) \
 && echo "deb https://deb.nodesource.com/node_$NODE_VERSION.x $codename main" > /etc/apt/sources.list.d/nodesource.list \
 && echo "deb-src https://deb.nodesource.com/node_$NODE_VERSION.x $codename main" >> /etc/apt/sources.list.d/nodesource.list \
 && apt_install nodejs
