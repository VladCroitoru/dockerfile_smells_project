FROM jdeathe/centos-ssh-apache-php:centos-6-httpd24u-php56u
MAINTAINER lanxianhui <lanxianhui@gmail.com>

ADD assets /assets
RUN bash /assets/setup.sh

# -----------------------------------------------------------------------------
# Set default environment variables used to configure the service container
# -----------------------------------------------------------------------------
ENV  SSH_AUTOSTART_SSHD=true \
     SSH_AUTOSTART_SSHD_BOOTSTRAP=true

CMD ["/usr/sbin/httpd-startup", "/usr/bin/supervisord", "--configuration=/etc/supervisord.conf"]
