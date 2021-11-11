FROM ubuntu:14.04
# not: debian:7.5 because chef-server needs GLIBC_2.14
MAINTAINER Ewa Czechowska <ewa@ai-traders.com>

#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

RUN mkdir /scripts
# do not add any comments after ADD or COPY or you get: "no such file or directory"
COPY scripts /scripts 
RUN /scripts/install_chef_server.sh && mv /scripts/image_metadata.txt /etc/docker_image_metadata.txt && /scripts/cleanup.sh


EXPOSE 443
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/usr/bin/run_chef_server.sh"]