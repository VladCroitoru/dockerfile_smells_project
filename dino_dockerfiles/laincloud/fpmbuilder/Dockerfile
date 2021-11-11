FROM laincloud/centos-lain:20170405

RUN yum install -y ruby-devel rpm-build \
    && yum clean all
RUN gem install --no-ri --no-rdoc fpm

RUN mkdir -p /rpmbuilder

WORKDIR /rpmbuilder