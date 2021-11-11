FROM bfren/alpine-s6:alpine3.14-2.2.20

EXPOSE 3310

ENV \
    # the number of times per day freshclam will run to update definitions
    CLAMAV_FRESH_PER_DAY=12

COPY ./overlay /
COPY ./CLAMAV_BUILD /tmp/VERSION

RUN bf-install
