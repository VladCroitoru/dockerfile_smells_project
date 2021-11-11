FROM debian:jessie-slim

LABEL name="gitlab-discord-bridge" \
version=$CONT_IMG_VER \
maintainer="Luis E Alvarado <admin@avnet.ws>" \
description="GitLab->Discord webhook bridge"

ARG CONT_IMG_VER
ENV CONT_IMG_VER ${CONT_IMG_VER:-v1.0}
ARG DEBIAN_FRONTEND=noninteractive

ENV PREQ_PACKAGES \
ca-certificates \
curl

ENV BUILD_PACKAGES \
python3 \
python3-pip

ENV RUNTIME_PACKAGES \
python3

# User configurable variables
ENV BRIDGE_URL https://api.github.com/repos/blha303/gitlab-discord-bridge/tarball

# install required packages
RUN echo "Installing essential packages..." \
 && apt-get -q update > /dev/null \
 && apt-get -qy install --no-install-recommends \
 $PREQ_PACKAGES > /dev/null 2>&1 \
# App/Work Dir
 && echo "Preparing app directory..." \
 && mkdir -p /usr/src/app \
 && cd /usr/src/app \
 && echo "Downloading latest build from GitHub..." \
 && curl -sSL "$BRIDGE_URL" | tar xz --strip=1 \
 && echo "Installing build packages..." \
 && apt-get -qy install --no-install-recommends \
 $BUILD_PACKAGES > /dev/null 2>&1 \
 && echo "Configuring pip..." \
 && pip3 install --upgrade pip setuptools > /dev/null 2>&1 \
 && echo "Installing app dependencies..." \
 && pip install --no-cache-dir -r requirements.txt > /dev/null 2>&1 \
# clean up
 && echo "Cleaning up..." \
 && apt-get remove --purge -qy \
 $PREQ_PACKAGES \
 $BUILD_PACKAGES $(apt-mark showauto) > /dev/null 2>&1 \
 && apt-get autoremove -qy > /dev/null \
 && apt-get clean -qy > /dev/null \
# install runtime packages
 && echo "Installing runtime packages..." \
 && apt-get -q update > /dev/null \
 && apt-get -qy install --no-install-recommends \
 $RUNTIME_PACKAGES > /dev/null 2>&1 \
 && rm -rf /var/lib/apt/lists/* \
 && ldconfig \
 && chmod +x app.py \
 && rm -rf /tmp/* \
 && echo "Done! Thanks for waiting~"

WORKDIR /usr/src/app

EXPOSE 25431

# TODO -- Verify if entrypoint script will be needed
CMD ["python3","./app.py"]