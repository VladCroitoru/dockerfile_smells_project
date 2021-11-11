FROM 1uptalent/ruby-2.0

RUN apt-get update
RUN apt-get install -y wget
RUN apt-get install -y libssl-dev libcurl3 libcurl3-gnutls libcurl4-openssl-dev git-core

RUN gem install bundler

# Copy the Gemfile and Gemfile.lock into the image.
# Temporarily set the working directory to where they are.
WORKDIR /tmp
ADD Gemfile Gemfile
ADD Gemfile.lock Gemfile.lock
RUN bundle install --system

ADD . /app
WORKDIR /app
RUN rm -Rf vendor .bundle
RUN mkdir -p /app/log

VOLUME /docker.sock

EXPOSE 80
CMD ["puma", "-p", "80"]
