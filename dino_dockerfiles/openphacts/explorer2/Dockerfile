FROM ubuntu:14.04
MAINTAINER "Stian Soiland-Reyes <orcid.org/0000-0001-9842-9718>"
WORKDIR /
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install ruby1.9.3 bundler libsqlite3-dev nodejs wget
COPY . /explorer2

ENV RAILS_ENV production
WORKDIR /explorer2
RUN bundle install
RUN cp config/database.yml_example config/database.yml
RUN cp config/environments/production.rb_example config/environments/production.rb
# We don't bother with an Apache/nginx for the assets
RUN sed -i 's/config.serve_static_assets.*/config.serve_static_assets = true/' config/environments/production.rb
RUN cp config/app_settings.yml_example config/app_settings.yml
RUN rake db:create:all
RUN rake db:migrate
RUN rake assets:precompile
WORKDIR /explorer2/filestore
## [2017.01.26] There is no 'explorer' directory in data.openphacts.org for any version newer than 1.4.
#RUN wget -q http://data.openphacts.org/1.4/explorer2/compounds.txt.bz2 http://data.openphacts.org/1.4/explorer2/compounds.txt.bz2.sha1
#RUN sha1sum -c compounds.txt.bz2.sha1
#RUN bunzip2 compounds.txt.bz2

WORKDIR /explorer2

#RUN rake explorer:load_all_assets

# URI for API (without trailing /)
ENV API_URL https://beta.openphacts.org/2.1
# Get your own key at https://dev.openphacts.org/admin/access_details
ENV API_APP_ID 161aeb7d
ENV API_APP_KEY cffc292726627ffc50ece1dccd15aeaf
ENV EXPLORER_MAINTENANCE FALSE
ENV ES_SEARCH_URL http://localhost:8839/search
ENV AUTOCOMPLETE_URL http://localhost:8839/autocomplete

EXPOSE 3000
ENTRYPOINT ["/explorer2/docker/entrypoint.sh"]
CMD ["rails", "server"]

