#
# Dockerfile
#
FROM mkovac/buster:latest
LABEL MAINTAINER="matej.kovac@gmail.com"

# files and scripts needed to build the image
#
COPY build /root/build

ARG CACHE_DATE=1970-01-01
RUN run-parts --report --exit-on-error /root/build/scripts && \
  rm -rfv /root/build

ENTRYPOINT ["/sbin/entrypoint.sh"]

CMD ["/bin/bash"]
