# match the Ruby version with GitHub Actions workflow:
FROM ruby:3.0.0-slim

WORKDIR /usr/src

#####
# Install Google Cloud SDK
#####

RUN apt-get update && apt-get install -y \
    curl \
    git \
    python

RUN curl https://sdk.cloud.google.com > /tmp/install-gcloud &&\
    chmod +x /tmp/install-gcloud &&\
    bash /tmp/install-gcloud --disable-prompts

#####
# Configure Google Cloud SDK
#####

RUN echo "source /root/google-cloud-sdk/completion.bash.inc" >> /root/.bashrc
RUN echo "source /root/google-cloud-sdk/path.bash.inc" >> /root/.bashrc
RUN bash -lc "gcloud components install kubectl"

#####
# Configure Ruby and co.
#####

# Configure Bundler to not install extra fluff with gems
RUN echo 'gem: --no-document' > /etc/gemrc
RUN gem install bundler

COPY Gemfile Gemfile.lock /usr/src/
RUN bundle install

COPY app /usr/src/
COPY config.yml /usr/src
ENTRYPOINT ["bash", "-lc", "bundle exec ruby turbulence.rb"]
