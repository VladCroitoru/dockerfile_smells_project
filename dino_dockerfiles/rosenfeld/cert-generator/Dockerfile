FROM ruby
RUN gem install --no-rdoc --no-ri rack puma rubyzip
COPY config.ru /
COPY app.rb /
COPY generate-certs /
COPY INSTRUCTIONS.html /
EXPOSE 80
ENV RACK_ENV production
CMD ["puma", "-p", "80"]
