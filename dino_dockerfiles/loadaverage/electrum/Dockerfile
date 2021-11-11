# version: 0.0.2
# description: Electrum BitCoin wallet in Docker container, this image uses X11 socket
#
# Howto:
#
#  build image
#   git clone https://github.com/loadaverage/electrum.git
#   cd electrum && docker build -t electrum .
#
#  run container
#   docker run --rm \
#        -v ~/.electrum:/home/electrum \
#        -v ~/.themes:/home/electrum/.themes:ro \
#        -v ~/.fonts:/home/electrum/.fonts:ro \
#        -v ~/.icons:/home/electrum/.icons:ro \
#        -v /usr/share/themes:/usr/share/themes:ro \
#        -v /usr/share/fonts:/usr/share/fonts:ro \
#        -v /tmp/.X11-unix:/tmp/.X11-unix \
#        -e DISPLAY=$DISPLAY electrum

FROM debian:stretch
LABEL maintainer="Vadim Sloun <github@roundside.com>"
ENV QT_X11_NO_MITSHM 1
RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update -qq && apt-get upgrade -yqq && \
  apt-get install electrum python-pbkdf2  python-qt4 --no-install-recommends -yqq && \
  useradd electrum -m -s /bin/bash 
USER electrum
CMD ["electrum"]
