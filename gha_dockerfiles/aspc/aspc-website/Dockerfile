FROM ruby:2.6.3 AS Core

# Update
RUN apt-get update && apt-get install -y npm && npm install -g yarn

#Add sudo just to simplify transfer process
RUN  apt-get -y install sudo

# Yarn / Node apt-get repositories - not sure if needed 
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list

# Google chrome apt-get repositories - not sure if needed
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

#added line due to not found error https://stackoverflow.com/questions/27423684/unable-to-locate-package-google-chrome-stable-ubuntu12-on-openstack
# RUN sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

# Dependencies for ASPC Main Site
RUN apt update
RUN apt-get -y install build-essential git nginx postgresql libpq-dev python-dev \
    libsasl2-dev libssl-dev libffi-dev gnupg2 nodejs \
    curl libjpeg-dev libxml2-dev libxslt-dev nodejs yarn \
    imagemagick google-chrome-stable

#To correct bundler 2 error https://stackoverflow.com/questions/53231667/bundler-you-must-use-bundler-2-or-greater-with-this-lockfile
RUN gem install bundler 

WORKDIR /aspc

COPY Gemfile Gemfile.lock /aspc/

#Install Gems 
RUN bundle install

COPY package.json yarn.lock /aspc/

RUN yarn install

EXPOSE 8080

COPY docker/entrypoint.sh /usr/bin/

RUN chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["entrypoint.sh"]

CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
