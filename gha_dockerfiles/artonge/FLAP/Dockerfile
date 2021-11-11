# syntax = docker/dockerfile:experimental

FROM debian:buster-slim

ARG CI_COMMIT_REF_NAME

COPY ./system/img_build/userpatches/overlay/install_flap.sh /install_flap.sh

# Make exported env var available during build on gitlab pipelines: https://docs.gitlab.com/ee/topics/autodevops/#custom-buildpacks
RUN /install_flap.sh $CI_COMMIT_REF_NAME

WORKDIR /opt/flap

CMD ["flapctl", "start"]
