FROM centos:latest
LABEL maintainer="omaciel@redhat.com"

RUN yum -y install https://yum.theforeman.org/releases/latest/el7/x86_64/foreman-release.rpm
RUN yum -y install https://yum.theforeman.org/releases/latest/el7/x86_64/foreman-release-scl-4-1.el7.noarch.rpm
RUN yum install -y tfm-rubygem-hammer_cli_foreman_admin

# Disable ssl verification
RUN echo ":ssl:" >> /etc/hammer/cli.modules.d/foreman.yml
RUN echo "  :verify_ssl: false" >> /etc/hammer/cli.modules.d/foreman.yml

ENTRYPOINT ["hammer"]
CMD ["--help"]
