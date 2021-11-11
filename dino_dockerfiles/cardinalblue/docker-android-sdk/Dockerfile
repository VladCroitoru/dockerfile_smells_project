FROM circleci/android:api-29
ADD Gemfile* ./
RUN sudo apt-get update \
    && sudo apt-get install build-essential make ruby-dev curl zlib1g-dev liblzma-dev \
    && sudo gem install bundler -v 1.16.0 \
    && bundle install \
    && sudo rm Gemfile*
CMD 'sh'
