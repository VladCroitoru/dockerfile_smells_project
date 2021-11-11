FROM hotio/debian-base
MAINTAINER hotio

# set build arg
ARG DEBIAN_FRONTEND=noninteractive

# install
RUN     apt-get update \
    &&  apt-get install -y \
            libcurl3 \
            libsqlite3-0 \
            libmono-cil-dev \
            mediainfo \
    &&  radarr_tag=$(curl -sX GET "https://api.github.com/repos/Radarr/Radarr/releases" | \
                        awk '/tag_name/{print $4;exit}' FS='[""]') \
    &&  mkdir -p /app \
    &&  curl -o /tmp/radarr.tar.gz -L \
            "https://github.com/Radarr/Radarr/releases/download/${radarr_tag}/Radarr.develop.${radarr_tag#v}.linux.tar.gz" \
    &&  tar ixzf /tmp/radarr.tar.gz -C /app --strip-components=1 \
    # clean up
    &&  apt-get autoremove -y \
    &&  apt-get clean \
    &&  rm -rf \
            /tmp/* \
            /var/lib/apt/lists/* \
            /var/tmp/*

# add local files
COPY root/ /

# ports and volumes
EXPOSE 7878
VOLUME ["/config"]
