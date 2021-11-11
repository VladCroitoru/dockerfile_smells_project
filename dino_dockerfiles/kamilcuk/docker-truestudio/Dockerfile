From finalduty/archlinux

Maintainer Kamil Cukrowski <kamilcukrowski@gmail.com>

# install packages
RUN set -xueo pipefail && \
  echo 'Install truestudio dependencies' && \
  echo -ne '[aur-archlinux]\nSigLevel=Never\nServer = https://repo.itmettke.de/aur/$repo/$arch\n' >> /etc/pacman.conf && \
  pacman --noconfirm -Sy webkitgtk && \
  echo '- SUCCESS prepare ------------------'

# some const dependent on version
ENV TRUESTUDIO_VER x86_64_v9.0.0_20180117-1023
ENV TRUESTUDIO_URL http://download.atollic.com/TrueSTUDIO/installers/Atollic_TrueSTUDIO_for_STM32_linux_${TRUESTUDIO_VER}.tar.gz

# download in one RUN
RUN set -xueo pipefail && \
  echo 'Downlad truestudio and check md5sum' && \
  echo ${TRUESTUDIO_URL} ${TRUESTUDIO_VER} && \
  curl -O ${TRUESTUDIO_URL}     && \
  curl -O ${TRUESTUDIO_URL}.MD5 && \
  md5sum -c $(basename ${TRUESTUDIO_URL}.MD5) && \
  rm $(basename ${TRUESTUDIO_URL}.MD5) && \
  echo '- SUCCESS download ----------------------------'

ENV TRUESTUDIO_INSTALL_PATH /opt/Atollic_TrueSTUDIO_for_STM32_9.0.0

# create links in ONE RUN
RUN set -xueo pipefail && \
  installPath=${TRUESTUDIO_INSTALL_PATH} && \
  echo 'Add truestudio tools and truestudio and headless.sh to PATH' && \
  echo 'PATH="$PATH:'"${installPath}"'/ARMTools/bin:'"${installPath}"'/PCTools/bin"' >> /etc/bash.bashrc && \
  ln -s "${installPath}/ide/TrueSTUDIO" /usr/bin/ && \
  echo -ne '#!/bin/sh\ncd '"${installPath}"'/ide\nexec ./headless.sh "$@"\n' > /usr/bin/headless.sh && \
  chmod +x /usr/bin/headless.sh && \
  echo '- SUCCESS postinstall --------------------------'

# install in the second RUN
RUN set -xueo pipefail && \
  echo 'Unpack and install truestudio' && \
  f=$(basename ${TRUESTUDIO_URL}) && \
  tar xzfvp $f && \
  installPath=${TRUESTUDIO_INSTALL_PATH} && \
  scriptPath=$(basename ${TRUESTUDIO_INSTALL_PATH})_installer && \
  cp ${scriptPath}/license.txt /ATOLLIC-END-USER-SOFTWARE-LICENSE-AGREEMENT && \
  mkdir -p ${installPath} && \
  tar xzvfp ${scriptPath}/install.data -C ${installPath} && \
  rm $f && rm -r ${scriptPath} && \
  echo '- SUCCESS installed ----------------------------'


