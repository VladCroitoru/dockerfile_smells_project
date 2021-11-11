FROM ruby:2.1
MAINTAINER Alain Beauvois <alain@questioncode.fr>

RUN mkdir -p /opt
RUN cd /opt && git clone https://github.com/ivaldi/brimir.git 

WORKDIR /opt/brimir

RUN apt-get update && apt-get -y install nodejs
RUN apt-get -y install mysql-client vim

RUN bundle install --without postgresql development test --deployment

RUN gem install dotenv dotenv-rails

ADD database.yml /opt/brimir/config/database.yml

EXPOSE 3000

RUN apt-get clean

ENV RAILS_ENV production

ENV DEVISE_SECRET_KEY ccaf6fd413c660bf798f5517a6278010355123171c51af97f6019dd69ed62571ee2b342aedef0b15a96ead2f1021c9ef4b4ac91fd2901cd3145965158258c39d
RUN echo "Devise.secret_key= ENV['DEVISE_SECRET_KEY']" >> /opt/brimir/config/initializers/devise.rb
ENV SECRET_KEY_BASE e1dd1f2fa691750f01e19de0ab7066263251d06a3c4a33ab5dfa6ab0500cd4911ab9e53c118587e91ccd9577dacb13b00b70692c79fc3818ee09a9395d372b3e
RUN tail /opt/brimir/config/initializers/devise.rb 

CMD rake db:create && rake db:schema:load && rake assets:precompile && perl -p -i -e 's/config.serve_static_assets .*/config.serve_static_assets = true/' config/environments/production.rb && rails server 

