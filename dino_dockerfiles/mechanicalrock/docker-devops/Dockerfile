FROM python:2.7

RUN apt-get update && apt-get install -y zip curl libgmp-dev
RUN pip install boto3==1.3.0

ADD ruby/install-rvm.sh /tmp/install/install-rvm.sh
RUN chmod u+x /tmp/install/install-rvm.sh
RUN /tmp/install/install-rvm.sh stable
RUN usermod -a -G rvm root

Add ruby/install-ruby.sh /tmp/install/install-ruby.sh
RUN chmod u+x /tmp/install/install-ruby.sh
RUN /tmp/install/install-ruby.sh 2.2.3 bundler rspec serverspec rake netaddr

SHELL [ "/bin/bash", "-l", "-c" ]
RUN gem install ci_reporter_rspec aws-sdk serverspec-aws ansible_spec

ADD .bashrc /.bashrc
CMD ["/bin/bash", "-l"]
