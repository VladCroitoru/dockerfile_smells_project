FROM ruby:2.3-slim

# Set Environment variables
ENV RACK_ENV development

# Install needed Linux packages
RUN apt-get update && \
    apt-get install -y git libxml2-dev libxslt-dev libcurl4-openssl-dev libpq-dev libsqlite3-dev build-essential postgresql libreadline-dev && \
    rm -rf /var/lib/apt/lists/*

# Create Directory
RUN mkdir /opt/stringer

# set the working directory
WORKDIR /opt/stringer

# Install bundler
RUN gem install bundler

# Copy the application into place
COPY . /opt/stringer

# Install Ruby Dependencies
RUN bundle install

# Expose the 'config'-directory as a volume, to be able to tweak things
VOLUME ["/opt/stringer/config"]

# Expose Port 5000
EXPOSE 5000

# run entrypoint.sh script, which does all the magic
CMD [ "/opt/stringer/docker/entrypoint.sh" ]
#CMD ["/bin/ls", "-lha", "/opt/stringer"]
