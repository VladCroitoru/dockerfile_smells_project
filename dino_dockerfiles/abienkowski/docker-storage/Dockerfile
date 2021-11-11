FROM debian:stretch
MAINTAINER Adrian Bienkowski (abienkow@uwo.ca)
# --
# -- NOTE: this image should be run with -v /etc/docker/plugins:/etc/docker/plugins
# --   so that the container can be responsible for setting itself up as a volume plugin
# --
# -- TODO: to expose the convoy binaries to at the host level need to run
# --   the docker image with -v /usr/local/bin:/usr/local/bin
# --
# -- environmnet variables used by container scripts
ENV CONVOY_DEVICE=sdb
# -- extract the released package onto the docker filesystem
ADD files/convoy.tar.gz /root/
# -- add dm helper script
ADD files/dm_dev_partition.sh /
# -- add the start script
ADD entrypoint-options.sh /
RUN chmod +x /entrypoint-options.sh
# -- set entrypoint to convoy executable so other options can be passed through CMD
ENTRYPOINT ["/usr/local/bin/convoy"]
# -- set command options
CMD ["/entrypoint-options.sh"]
