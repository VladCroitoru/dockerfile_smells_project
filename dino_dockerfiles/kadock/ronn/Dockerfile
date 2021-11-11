FROM ruby:2.3
COPY ronn.sh /usr/local/bin/ronn.sh
RUN gem install ronn && chmod +x /usr/local/bin/ronn.sh
ENTRYPOINT ["/usr/local/bin/ronn.sh"]
