FROM jekyll/jekyll

# Install Jekyll
RUN gem install bundler jekyll

# Setting workdir will also create the dir if it doesn't exist, so no need to mkdir
WORKDIR /site

# Copy the Gemfile and Gemfile.lock into the image and run bundle install in a
# way that will be cached
ADD docs/Gemfile Gemfile
ADD docs/Gemfile.lock Gemfile.lock

# RUN touch Gemfile.lock
RUN chmod a+w Gemfile.lock

RUN bundle install

# Jekyll runs on port 4000 by default
EXPOSE 4000

CMD ["jekyll", "serve"]