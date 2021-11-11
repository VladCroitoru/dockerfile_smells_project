FROM ruby:2.2.2
MAINTAINER James Cuzella (@trinitronx)

RUN apt-get install -y git

# Copy the Gemfile and Gemfile.lock into the image.
# Temporarily set the working directory to where they are.
WORKDIR /tmp
ADD ./Gemfile Gemfile
ADD ./Gemfile.lock Gemfile.lock
RUN bundle install

# Everything up to here was cached. This includes
# the bundle install, unless the Gemfiles changed.
# Now copy the app into the image.
ADD . /opt/app

# Set the final working dir to the Rails app's location.
WORKDIR /opt/app

# Set up a default runtime command
CMD ./jenkins-job-batch-git-clone.rb

