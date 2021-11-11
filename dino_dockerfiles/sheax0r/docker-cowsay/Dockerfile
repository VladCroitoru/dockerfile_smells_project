FROM centos:centos6

# EPEL
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

# Packages
RUN yum install -y ImageMagick git which tar cowsay gcc-c++ make rubygems && yum clean all

# RVM
RUN curl -sSL https://rvm.io/mpapis.asc | gpg2 --import -
RUN curl -L get.rvm.io | bash -s stable
RUN source /etc/profile.d/rvm.sh
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 2.0"

# Hack to deal with rubygems DDOS - remove this!
RUN echo -ne "\n54.186.104.15 api.rubygems.org" >> /etc/hosts
RUN /bin/bash -l -c "gem install --no-ri --no-rdoc bundler"

# Install it.
RUN curl -L https://github.com/sheax0r/cowsapi/archive/v0.1.1.tar.gz | tar xz
RUN ln -s /cowsapi-0.1.1 /cowsapi
RUN cd /cowsapi && bash -l -c "bundle install"

# Get ready to run it
ADD run.sh /run.sh
ENTRYPOINT ["/run.sh"]
EXPOSE 80

