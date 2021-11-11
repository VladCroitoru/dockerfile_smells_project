FROM         base/archlinux

MAINTAINER   Pedro Flores <pflores@codelab.com.py>

RUN          pacman-key --refresh-keys && \
             pacman -Syu --noconfirm && \
             pacman-db-upgrade && \
             pacman -S --noconfirm npm openssl git && \
             pacman -Scc --noconfirm && \
             useradd -m yolomer && \
             export INSTALLED_USER=yolomer && \
             su - -c 'mkdir "${HOME}/.npm-packages"' $INSTALLED_USER && \
             su - -c 'echo "prefix=${HOME}/.npm-packages" >> ~/.npmrc' $INSTALLED_USER && \
             su - -c 'echo "NPM_PACKAGES=\"${HOME}/.npm-packages\"" >> ~/.bashrc' $INSTALLED_USER && \
             su - -c 'echo "PATH=\"\$NPM_PACKAGES/bin:\$PATH\"" >> ~/.bashrc' $INSTALLED_USER && \
             su - -c 'npm install -g npm@latest' $INSTALLED_USER && \
             su - -c 'npm install -g bower gulp grunt-cli yo' $INSTALLED_USER
