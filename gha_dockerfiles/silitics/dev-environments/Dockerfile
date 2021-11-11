FROM ubuntu:20.04

ARG VARIANT=minimal

ARG FEATURES=

ARG USERNAME=dev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

COPY . /usr/local/silitics/dev-environments

RUN /usr/local/silitics/dev-environments/scripts/install-devctrl.sh

RUN devctrl run install-features

USER ${USERNAME}
