FROM centos:7
SHELL ["/bin/bash", "-l", "-c"]

ENV SCALARM_HOME /scalarm

RUN yum install -y curl which git

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN curl -sSL https://get.rvm.io | bash -s stable
RUN source /etc/profile.d/rvm.sh

RUN rvm requirements
RUN rvm install 2.3
RUN gem install bundler --no-ri --no-rdoc

ADD . $SCALARM_HOME

WORKDIR $SCALARM_HOME

EXPOSE 3002

RUN bundle config git.allow_insecure true
RUN bundle install

CMD /bin/bash -c "rake service:start"
