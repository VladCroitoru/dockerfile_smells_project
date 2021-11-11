FROM jekyll/jekyll

ADD Gemfile /srv/jekyll
RUN bundle install

EXPOSE 4000

CMD jekyll serve