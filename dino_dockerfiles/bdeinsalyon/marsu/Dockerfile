FROM ruby:2.3.3
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs

# Prepare /app directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
ADD Gemfile /app/Gemfile
ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install

# Define environment variables
ENV DATABASE_URL postgres://postgres/marsu
ENV AZURE_CLIENT_ID ""
ENV AZURE_CLIENT_SECRET ""
ENV AZURE_TENANT_ID ""
ENV RAILS_ENV production
ENV PORT 3000
ENV WEB_HOST "adhesion.bde-insa-lyon.fr"
ENV WEB_PORT 80
ENV MAILGUN_API_KEY ""
ENV MAILGUN_DOMAIN ""
ENV RAILS_LOG_TO_STDOUT ""
ENV RAILS_SERVE_STATIC_FILES "true"
ENV SECRET_KEY_BASE "qsdfjqmlsdfkjocnzqeifzehdeoefqdjsoipcfhbkjdxdxjggfkgvdforshfyg"
ENV ROBOT_EMAIL "robot@bde-insa-lyon.fr"

# Copy app files (see .dockerignore for ignored files)
ADD . /app
VOLUME /app/public/assets
RUN chmod +x /app/bin/marsu

EXPOSE 3000

CMD /app/bin/marsu