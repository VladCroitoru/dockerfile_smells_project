FROM ubuntu:xenial

ARG USERNAME=windyakin

RUN sed -i.bak -e "s%http://archive.ubuntu.com/ubuntu/%http://ftp.jaist.ac.jp/pub/Linux/ubuntu/%g" /etc/apt/sources.list

RUN apt-get update \
   && apt-get dist-upgrade -y \
   && apt-get install -y sudo git zsh software-properties-common build-essential curl file python-setuptools ruby \
   && rm -rf /var/lib/apt/lists/*

# For jp_JP.UTF-8 and JST(Asia/Tokyo)
ENV TZ Asia/Tokyo
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:en
ENV LC_ALL ja_JP.UTF-8
RUN apt-get update \
  && apt-get install -y language-pack-ja tzdata \
  && rm -rf /var/lib/apt/lists/* \
  && update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja" \
  && echo "${TZ}" > /etc/timezone \
  && rm /etc/localtime \
  && ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
  && dpkg-reconfigure -f noninteractive tzdata

# adduser ${USERNAME}:${USERNAME} with password '${USERNAME}'
RUN groupadd -g 1000 ${USERNAME} \
   && useradd -g ${USERNAME} -G sudo -m -s /bin/bash ${USERNAME} \
   && echo "${USERNAME}:${USERNAME}" | chpasswd

RUN echo "Defaults visiblepw" >> /etc/sudoers
RUN echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN git clone https://github.com/Linuxbrew/brew.git /home/${USERNAME}/.linuxbrew \
  && chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/.linuxbrew \
  && sudo -u ${USERNAME} echo "PATH=/home/${USERNAME}/.linuxbrew/bin:/home/${USERNAME}/.linuxbrew/sbin:$PATH" > /home/${USERNAME}/.bashrc

ADD . /home/${USERNAME}/dotfiles
RUN chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/dotfiles \
  && sudo -u ${USERNAME} -i /home/${USERNAME}/dotfiles/setup.sh

USER ${USERNAME}
WORKDIR /home/${USERNAME}/
CMD ["zsh"]
