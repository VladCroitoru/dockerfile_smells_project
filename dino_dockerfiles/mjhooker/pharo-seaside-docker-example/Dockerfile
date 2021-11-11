# -*- sh -*-
FROM mjhooker/archlinux-pharo-image
MAINTAINER mjhooker, mjhooker@gmail.com

ADD . /home/deploy

EXPOSE 8080

#CMD ./pharo Pharo.image ./deploy/zinc.st
CMD ./pharo Pharo.image ./deploy/seaside.st
