FROM ubuntu:17.10

ADD . /ruby-app
WORKDIR /ruby-app
RUN /usr/bin/apt-get update \
   && /usr/bin/apt-get install --no-install-recommends -qy ruby ruby-dev make g++ && gem install bundler --no-ri --no-rdoc \
   && /usr/bin/env bundle install --without test development \
   && /usr/bin/apt-get -qy purge ruby-dev make g++ \
   && /usr/bin/apt-get -qy autoremove \
   && /bin/rm -rf /var/lib/gems/2.3.0/cache /var/cache/* /var/lib/apt/lists/*
USER www-data
EXPOSE 8080
ENV RAILS_ENV=production
ENTRYPOINT ["/usr/bin/ruby", "/usr/local/bin/bundle", "exec"]
CMD ["/usr/local/bin/unicorn", "-o", "0.0.0.0", "-p", "8080", "-c", "unicorn.rb"]
