FROM etna-base
# Perform these steps first to allow better caching behavior
COPY Gemfile Gemfile.lock /app/
RUN bundle install
COPY package.json package-lock.json /app/
RUN npm install
COPY . /app/

ARG APP_NAME
ARG FULL_BUILD=1
RUN /entrypoints/build.sh
RUN npm run build
