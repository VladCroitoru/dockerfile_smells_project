FROM ubuntu:16.04

# Locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Update Apt Packages
RUN apt-get update && apt-get -qy upgrade

# Install Apt Packages
RUN apt-get update && apt-get install -y \
  software-properties-common \
  python-software-properties \
  ca-certificates \
  locales \
  unzip \
  curl \
  ffmpeg \
  lame

# Add Oracle Java Repo
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true \
  | /usr/bin/debconf-set-selections
RUN add-apt-repository ppa:webupd8team/java && \
  apt-get update && apt-get install -y \
  oracle-java8-installer \
  oracle-java8-set-default

# Get Subsonic stand-alone package
ENV SUBSONIC_HOME /var/subsonic
ENV PKG_VER 6.0

RUN mkdir ${SUBSONIC_HOME}
RUN curl http://subsonic.org/download/subsonic-${PKG_VER}-standalone.tar.gz \
  | tar zx -C ${SUBSONIC_HOME}/

# Link transcoders
ENV SUBSONIC_TRANSCODE_FOLDER ${SUBSONIC_HOME}/transcode
RUN mkdir -p ${SUBSONIC_TRANSCODE_FOLDER} && \
  ln -fs /usr/bin/ffmpeg /usr/bin/lame ${SUBSONIC_TRANSCODE_FOLDER}

# Mount external volume
ENV SUBSONIC_DB_FOLDER  ${SUBSONIC_HOME}/db
ENV SUBSONIC_MUSIC_FOLDER /mnt/media/Music
ENV SUBSONIC_PODCAST_FOLDER /mnt/media/Podcast
ENV SUBSONIC_PLAYLIST_FOLDER /mnt/media/Playlists
VOLUME ${SUBSONIC_DB_FOLDER}
VOLUME ${SUBSONIC_MUSIC_FOLDER}
VOLUME ${SUBSONIC_PODCAST_FOLDER}
VOLUME ${SUBSONIC_PLAYLIST_FOLDER}

# Expose http/https
ENV SUBSONIC_PORT 4040
ENV SUBSONIC_HTTPS_PORT 4050
EXPOSE ${SUBSONIC_PORT}
EXPOSE ${SUBSONIC_HTTPS_PORT}

# Entry point
ADD ./launch_subsonic.sh /launch_subsonic.sh
RUN chmod +x  /launch_subsonic.sh

ENTRYPOINT ["/launch_subsonic.sh"]
