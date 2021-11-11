FROM phusion/passenger-ruby21:0.9.14

# Set correct environment variables.
ENV HOME /root
ENV RAILS_ENV production

ADD . /home/app

# Make sure we didn't accidentally include a pid file.
RUN /bin/bash -c -l 'rm -f /home/app/tmp/pids/server.pid'

WORKDIR /home/app
RUN /bin/bash -c -l 'gem install foreman'
RUN /bin/bash -c -l 'bundle install'

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80

CMD /bin/bash -c -l 'cd /home/app && bundle exec rake db:create && bundle exec rake db:migrate && foreman run bundle exec rails server -p 80'
