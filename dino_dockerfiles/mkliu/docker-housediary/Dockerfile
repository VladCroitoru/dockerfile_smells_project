FROM     mkliu/docker-ionic
MAINTAINER wayliu [at] live [dot] com

RUN git clone https://github.com/wizky/housediary.git /housediary
RUN cd /housediary

EXPOSE 8100
EXPOSE 35729

WORKDIR housediary
CMD ionic serve 8100 35729
