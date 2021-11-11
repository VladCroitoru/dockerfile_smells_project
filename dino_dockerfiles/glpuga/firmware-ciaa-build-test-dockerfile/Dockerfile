#
# Starting image from LTS Ubuntu 16.04
FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential curl gdb git php-cli ca-certificates

WORKDIR /root

COPY files/* ./

ENTRYPOINT ["/root/entrypoint.sh"]
