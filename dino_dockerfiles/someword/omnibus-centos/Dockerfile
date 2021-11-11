FROM centos:centos6
MAINTAINER Derek Olsen 

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN rpm -ivh http://download.fedoraproject.org/pub/epel/6/$(arch)/epel-release-6-8.noarch.rpm
RUN yum install -y centos-release-SCL 
RUN yum groupinstall -y 'Development Tools' 

RUN yum install -y \
    openssl-devel \
    expat-devel \
    perl-ExtUtils-MakeMaker \
    curl-devel \
    golang \
    ruby193 \
    ruby193-ruby-devel 

RUN yum remove -y git
# Work around git/go version issues on centos - https://twitter.com/gniemeyer/status/472318780472045568

RUN cd /usr/src && curl -o git-1.9.4.tar.gz https://www.kernel.org/pub/software/scm/git/git-1.9.4.tar.gz && tar xzf git-1.9.4.tar.gz && cd git-1.9.4 && make prefix=/usr all && make prefix=/usr install 

RUN echo "export PATH=\${PATH}:/opt/rh/ruby193/root/usr/local/bin" | tee -a /opt/rh/ruby193/enable
RUN source /opt/rh/ruby193/enable

RUN cp /opt/rh/ruby193/enable /etc/profile.d/ruby193.sh

RUN git config --global user.email "docker@flapjack.io" && \
    git config --global user.name "Flapjack Docker Packager"

RUN /bin/bash -l -c "git clone https://github.com/flapjack/omnibus-flapjack.git && cd omnibus-flapjack && bundle install --binstubs" 
