# Dockerfile to have a running centos7 installation with chefdk
FROM centos:7

RUN rpm --import https://downloads.chef.io/packages-chef-io-public.key
RUN echo -e "[chef-stable]\nname=chef-stable\nbaseurl=https://packages.chef.io/stable-yum/el/7/\$basearch/ \ngpgcheck=1 \nenabled=1" > chef-stable.repo
RUN cat chef-stable.repo
RUN mv chef-stable.repo /etc/yum.repos.d/
RUN curl -fsSL https://get.docker.com/ | sh
RUN yum makecache fast
RUN yum groupinstall -y "Development Tools"
RUN yum install -y python-yaml python-setuptools
RUN yum install -y chefdk-0.13.21-1.el7 \
&& /opt/chefdk/bin/chef gem install --no-ri --no-rdoc kitchen-docker -v 2.4.0 \
&& /opt/chefdk/bin/chef gem install --no-ri --no-rdoc kitchen-openstack -v 3.0.0 \
&& yum clean all

# Set ChefDK paths
ENV PATH="/opt/chefdk/bin:/root/.chefdk/gem/ruby/2.1.0/bin:/opt/chefdk/embedded/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV GEM_ROOT="/opt/chefdk/embedded/lib/ruby/gems/2.1.0"
ENV GEM_HOME="/root/.chefdk/gem/ruby/2.1.0"
ENV GEM_PATH="/root/.chefdk/gem/ruby/2.1.0:/opt/chefdk/embedded/lib/ruby/gems/2.1.0"

# Set locale
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
