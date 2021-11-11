FROM ubuntu:14.04

ENV DEBIAN_FRONTEND=noninteractive

RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:skunk/pepper-flash && \
  apt-get update && \
  apt-get install -y chromium-browser chromium-browser-l10n pepflashplugin-installer \
                     fonts-takao x11vnc xvfb openssh-server supervisor && \
  apt-get autoclean && \
  apt-get autoremove && \
  rm -rf /var/lib/apt/lists/* && \
  locale-gen en_US.UTF.8 && \
  echo ". /usr/lib/pepflashplugin-installer/pepflashplayer.sh" >> /etc/chromium-browser/default && \
  echo "vncuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
  useradd -ms /bin/bash vncuser && \
  sed -i -E 's/^#?PermitRootLogin .*/PermitRootLogin no/g' /etc/ssh/sshd_config && \
  sed -i -E 's/^#?PasswordAuthentication .*/PasswordAuthentication no/g' /etc/ssh/sshd_config && \
  echo "AllowUsers vncuser" >> /etc/ssh/sshd_config && \
  mkdir /data

COPY data /data
USER vncuser
WORKDIR /home/vncuser

CMD ["sudo", "-E", "sh", "/data/run.sh"]
