FROM ansible/ansible:centos7

RUN yum install -y ruby ruby-dev gem rake 

RUN gem install serverspec

CMD ["/sbin/init"]
