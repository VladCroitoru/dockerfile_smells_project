FROM alpine:latest

COPY settings/repositories /etc/apk/repositories
# Installing build tools, chromium and an X server
RUN apk --update add \
  bash \
  tar \
  git \
  dpkg \
  python \
  make \
  g++ \
  openssh-client \
  xvfb \
  chromium \
  nodejs

# Patching the launch command to goes through xvfb
COPY settings/xvfb-chromium.sh /usr/bin/xvfb-chromium
RUN chmod 755 /usr/bin/xvfb-chromium
RUN ln -fs /usr/bin/xvfb-chromium /usr/bin/google-chrome
RUN ln -fs /usr/bin/xvfb-chromium /usr/bin/chromium-browser

RUN addgroup staff
RUN adduser -D -g "" -G staff -s /bin/bash devuser
RUN echo "devuser ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
RUN touch /home/devuser/.bashrc
RUN chown devuser:staff /home/devuser/.bashrc

# Installing the JS toolchain
RUN npm install -g bower
RUN npm install -g gulp
RUN npm install -g yo
