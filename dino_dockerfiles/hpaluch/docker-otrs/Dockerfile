# Builds OTRS-3.2 with MySQL in single container - suitable for development
# and testing of deployments

# Based on https://github.com/dockerfiles/centos-lamp

# To build OTRS image use:
#    sudo docker build -t MY_OTRS_IMAGE .
# To run
#    sudo docker run -P -d --name=MY_OTRS_INSTANCE MY_OTRS_IMAGE
# Later run 
#    sudo docker ps
# To see external ports mapping (typically 4915X)
# OTRS URL: http://YOUR_HOST:PORT/otrs/index.pl
# OTRS admin login/password: root@localhost/root
# SSH  login/password: root/changeme

FROM centos:centos6


# bootstrap otrs
ADD setup-otrs /opt/setup-otrs
RUN /opt/setup-otrs/prepare_os.sh
RUN /opt/setup-otrs/bootstrap_otrs.sh
ADD supervisord.conf /etc/

# export SSH port
EXPOSE 22
# export Apache ports
EXPOSE 80 443
CMD ["supervisord", "-n"]

