FROM scalarm/centos-base:17.09
SHELL ["/bin/bash", "-l", "-c"]

ENV SCALARM_HOME /scalarm

ADD . $SCALARM_HOME

WORKDIR $SCALARM_HOME
EXPOSE 3000

RUN bundle config git.allow_insecure true
RUN bundle config build.ruby-debug-ide --with-ruby-include=$rvm_path/src/ruby-2.3.4
RUN bundle config build.debase --with-ruby-include=$rvm_path/src/ruby-2.3.4
RUN bundle install

CMD /bin/bash -c "rake service:start" 
