FROM amazonlinux

RUN curl -sL https://rpm.nodesource.com/setup_6.x | bash - \
  && yum -y install nodejs \
  && yum -y install gcc-c++ make

CMD [ "node" ]