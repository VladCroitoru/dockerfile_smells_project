FROM nacyot/ruby-ruby:2.1.2
MAINTAINER Daekwon Kim <propellerheaven@gmail.com>

# Install Bundler
RUN gem install bundler --no-rdoc --no-ri
RUN ln -s /root/.rbenv/versions/2.1.2/bin/bundle /usr/local/bin

# Set workdir
WORKDIR /opt/hanginim

# Install dependencies
ADD ./Gemfile /opt/hanginim/Gemfile
ADD ./Gemfile.lock /opt/hanginim/Gemfile.lock
RUN bundle install

# Add application to image
ADD ./lib /opt/hanginim/lib
ADD ./data /opt/hanginim/data
ADD ./bin /opt/hanginim/bin
RUN touch .env

# Set enviroment variables
ENV TEAM TEAM
ENV CHANNEL CHANNEL
ENV NAME NAME
ENV INCOMING_TOKEN I_TOKEN
ENV OUTGOING_TOKEN O_TOKEN

# Expose port
EXPOSE 4567

# Set command
CMD ["ruby", "./bin/run.rb"]
