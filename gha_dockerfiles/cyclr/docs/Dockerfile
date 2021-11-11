FROM jekyll/jekyll

WORKDIR /opt/jekyll/
ADD Gemfile /opt/jekyll/
ADD Gemfile.lock /opt/jekyll/
RUN bundle install

VOLUME /jekyll

EXPOSE 4000

WORKDIR /jekyll
CMD jekyll serve --port 4000 --host 0.0.0.0
