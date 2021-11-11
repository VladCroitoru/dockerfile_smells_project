FROM ruby:2.2.0

ENV DEV /home/dev

RUN apt-get update -qq && \
    apt-get install -qy \
            python \
            python-dev \
            python-pip

# Install tutum-cli
RUN pip install tutum

# Copy the Gemfile and Gemfile.lock into the image.
COPY Gemfile $DEV/
COPY Gemfile.lock $DEV/

# Install ruby gems.
RUN cd $DEV && bundle install

COPY . $DEV

WORKDIR $DEV

ENTRYPOINT ["bundle", "exec" , "rake"]
