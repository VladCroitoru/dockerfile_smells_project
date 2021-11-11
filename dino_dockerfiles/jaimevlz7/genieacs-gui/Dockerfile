FROM ruby:2.3

MAINTAINER Jaime Vélez - Ingeniero Télemático.

# Nodejs is needed
RUN apt-get update -y && apt-get dist-upgrade -y && apt-get install nodejs -y

# Download GenieACS GUI
RUN cd /opt && git clone https://github.com/zaidka/genieacs-gui.git

# Work on the GUI
WORKDIR /opt/genieacs-gui

# Setup GenieACS GUI
RUN rm -f Gemfile.lock
RUN cp config/graphs-sample.json.erb config/graphs.json.erb
RUN cp config/index_parameters-sample.yml config/index_parameters.yml
RUN cp config/summary_parameters-sample.yml config/summary_parameters.yml
RUN cp config/parameters_edit-sample.yml config/parameters_edit.yml
RUN cp config/parameter_renderers-sample.yml config/parameter_renderers.yml
RUN cp config/roles-sample.yml config/roles.yml
RUN cp config/users-sample.yml config/users.yml
COPY development.rb config/environments/development.rb
COPY production.rb config/environments/production.rb
COPY test.rb config/environments/test.rb
RUN bundle
RUN bin/rake db:migrate RAILS_ENV=development

# Expose GenieACS GUI port
EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
