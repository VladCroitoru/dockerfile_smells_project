FROM rails

# update the operating system:
RUN apt-get update 

# if you need "vi" and "less" for easier troubleshooting later on:
RUN apt-get install -y vim; apt-get install -y less

# copy the ProvisioningEngine app to the container:
ADD . /ProvisioningEngine

# Define working directory:
WORKDIR /ProvisioningEngine

# Install the Rails Gems and prepare the database:
# note: the DOCKER=true is needed for filtering the gem rails-erd during the bundle install (in Gemfile: gem "rails-erd" if ENV["DOCKER"].nil?)
RUN export DOCKER=true; bundle install; bundle exec rake db:migrate RAILS_ENV=development

# expose tcp port 80
EXPOSE 80

# default command: run the web server on port 80 and on IP 0.0.0.0 (if the latter is missing, I have seen connection refused messages):
CMD ["rails", "server", "-p", "80", "-b", "0.0.0.0"]
