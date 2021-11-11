FROM phusion/passenger-full:1.0.9
LABEL maintainer="mfenner@datacite.org"

# Install Ruby 2.6.5
RUN bash -lc 'rvm --default use ruby-2.6.5'

ENV PATH="/usr/local/rvm/gems/ruby-2.6.5/bin:${PATH}"

# Update installed APT packages, clean up APT when done.
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install maltese gem
RUN /sbin/setuser app gem install maltese -v 0.9.12

CMD maltese sitemap --sitemap_bucket $SITEMAP_BUCKET --rack_env $RACK_ENV --access_key $AWS_ACCESS_KEY_ID --secret_key $AWS_SECRET_ACCESS_KEY --region $AWS_REGION --slack_webhook_url $SLACK_WEBHOOK_URL
