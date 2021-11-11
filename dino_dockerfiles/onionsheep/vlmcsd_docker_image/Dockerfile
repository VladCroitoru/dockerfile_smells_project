FROM centos:latest
MAINTAINER Liu Cong <onion_sheep@163.com>

COPY ./vlmcsd-x64-musl-static /root/vlmcsd
RUN chown root:root /root/vlmcsd
RUN chmod 0755 /root/vlmcsd

EXPOSE 1688

CMD ["/root/vlmcsd", "-D"]
