FROM ruby:2.7.4

WORKDIR /app

ENV LANG=C.UTF-8 \
    BUNDLE_JOBS=4 \
    BUNDLE_RETRY=3 \
    PATH=/app/bin:$PATH

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install


RUN gem update --system && \
    gem install bundler

COPY . /app
