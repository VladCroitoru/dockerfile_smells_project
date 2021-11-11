FROM ubuntu:18.04

LABEL maintainer="Ian Martin <ian@imartin.net>" license="MIT" description="Distrubuted NodeJS app for automated ripping and encoding media"
ENV DISPLAY=":0" LANG=C.UTF-8 DEBIAN_FRONTEND=noninteractive NODE_ENV=production U=2007 NO_UPDATE_NOTIFIER=true BABEL_DISABLE_CACHE=1

RUN apt-get -qq update && \
  apt-get install -yq gnupg && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8771ADB0816950D8 && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 8540356019f7e55b && \
  echo 'deb http://ppa.launchpad.net/heyarje/makemkv-beta/ubuntu bionic main' > /etc/apt/sources.list.d/makemkv.list && \
  echo 'deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu bionic main' > /etc/apt/sources.list.d/handbrake.list && \
  apt-get -qq update && \
  apt-get install -yq git makemkv-oss makemkv-bin curl ffmpeg libbluray-bin lsdvd dvdbackup libdvd-pkg handbrake-cli libcdio-utils cdparanoia && \
  dpkg-reconfigure libdvd-pkg && \
  apt-get clean && \
  groupadd -fg ${U} ncodr && \
  useradd --create-home --uid ${U} --gid ${U} ncodr && \
  passwd -l ncodr && \
  mkdir -p /media /rips && \
  chown -R ${U}:0 /media /rips && \
  chmod 4755 /usr/bin/bd_info

COPY [".", "/app/"]
WORKDIR /app
RUN apt-key adv --fetch-keys http://deb.nodesource.com/gpgkey/nodesource.gpg.key && \
  echo "deb http://deb.nodesource.com/node_10.x bionic main" >> /etc/apt/sources.list && \
  apt-get -qq update && \
  apt-get install -yq nodejs && \
  apt-get clean && \
  NODE_ENV=development npm install && \
  npm run build && \
  rm -rf node_modules && \
  npm install && \
  chown -R ${U}:0 /app

USER ${U}
EXPOSE 2000
HEALTHCHECK --start-period=15s --timeout=5s CMD /usr/bin/pgrep node
VOLUME ["/media"]
ENTRYPOINT ["/usr/bin/npm"]
CMD ["start"]
