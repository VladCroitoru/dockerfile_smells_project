#
# Flexget Dockerfile
#
# https://github.com/kmb32123/flexget-dockerfile
#

# Pull base image.
FROM python:2-onbuild

VOLUME ["/flexget"]
VOLUME ["/input"]
VOLUME ["/output"]

WORKDIR /flexget

CMD rm -f /flexget/.config-lock && flexget daemon start
