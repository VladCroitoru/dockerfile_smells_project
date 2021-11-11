FROM ruby:2.5.8-alpine3.12

# -----------------------------------------------------------------------------

# Install bundle & libraries and/or headers needed by some ruby deps' compilation (those with native-extensions, e.g. eventmachine)

RUN apk update && \
    apk add gcc make libc-dev g++

# Install git, for otherwise the *.gemspec installation of jekyll-theme-hydeout will not work
RUN apk add git

# -----------------------------------------------------------------------------

# Install ruby dependencies

RUN mkdir /myapp/
WORKDIR /myapp/

COPY Gemfile* *.gemspec /myapp/
# If we have the gem files already, the following will install the right version of bundler
RUN gem install bundler

RUN bundle install

# -----------------------------------------------------------------------------

# Activate if wanted: copy all existing files from tagtog-doc folder, to have default documentation

COPY . /myapp/

# -----------------------------------------------------------------------------

EXPOSE 4000

# See jekyll parameters: https://jekyllrb.com/docs/configuration/options/#serve-command-options
# "--incremental" can be faster, but is too conversative with the cache (https://jekyllrb.com/docs/configuration/incremental-regeneration/#incremental-regeneration)
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
CMD ["--livereload", "--incremental"]
