FROM ruby:2.4

# Setting workspace
RUN mkdir -p /app
WORKDIR /app

# Setting output directory
RUN mkdir -p /app/output
ENV OUTPUT_DIR=/app/output
VOLUME /app/output

# Copying application files to image
COPY find_line.rb /app/find_line.rb
COPY custom_logger.rb /app/custom_logger.rb
# COPY Gemfile /app/Gemfile

# Line ending conversion - necessary if building under Windows
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix * && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

# Installing application dependencies - unnecessary in current version
# RUN gem install bundler && bundler

# Setting entrypoint
ENTRYPOINT ["/app/find_line.rb"]