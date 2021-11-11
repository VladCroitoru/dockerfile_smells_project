FROM ruby:2.1-onbuild
ADD postkubevents.rb .
ADD testapi.rb .
ADD Gemfile .
ADD Gemfile.lock .
CMD ["./testapi.rb"]
