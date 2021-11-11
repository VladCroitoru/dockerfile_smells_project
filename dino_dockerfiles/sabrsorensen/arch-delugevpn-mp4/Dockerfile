FROM binhex/arch-delugevpn

ARG BUILD_DATE="unknown"
ARG COMMIT_AUTHOR="unknown"
ARG VCS_REF="unknown"
ARG VCS_URL="unknown"

LABEL maintainer=${COMMIT_AUTHOR} \
    org.label-schema.vcs-ref=${VCS_REF} \
    org.label-schema.vcs-url=${VCS_URL} \
    org.label-schema.build-date=${BUILD_DATE}

RUN \
  pacman -Syu --noconfirm && \
  pacman -S --needed --noconfirm \
        ffmpeg \
        gcc \
        git \
        python-pip && \
  pacman -Scc --noconfirm

RUN \
  git clone --depth 1 --single-branch git://github.com/mdhiggins/sickbeard_mp4_automator.git /sickbeard_mp4_automator/ && \
  pip install --no-cache-dir --upgrade -r /sickbeard_mp4_automator/setup/requirements.txt && \
  chmod a+rwx -R /sickbeard_mp4_automator && \
  ln -s /downloads /data && \
  ln -s /config_mp4_automator/autoProcess.ini /sickbeard_mp4_automator/autoProcess.ini && \
  rm -rf /sickbeard_mp4_automator/post_process && \
  ln -sf /config_mp4_automator/post_process /sickbeard_mp4_automator/

VOLUME /config_mp4_automator
