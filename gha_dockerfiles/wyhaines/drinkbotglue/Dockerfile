# Dockerfile.rails
FROM ruby:3.0.2
RUN apt-get update -qq \
&& apt-get install -y nodejs postgresql-client
ADD . /Rails-Docker
WORKDIR /Rails-Docker
RUN bundle install
EXPOSE 3000
CMD ["bash"]