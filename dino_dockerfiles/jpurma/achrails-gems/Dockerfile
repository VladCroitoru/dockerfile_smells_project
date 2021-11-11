FROM learninglayers/ror
MAINTAINER Jukka Purma <jukka.purma ÄT aalto.fi>

# this creates a ruby-on-rails image where gems are built and installed, to speed up creating new 
# development environments 
WORKDIR /tmp
COPY Gemfile Gemfile
COPY Gemfile.lock Gemfile.lock
RUN bundle install
