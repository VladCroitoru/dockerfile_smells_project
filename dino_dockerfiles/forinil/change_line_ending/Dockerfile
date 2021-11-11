FROM ruby:2.4

# Setting workspace
RUN mkdir -p /app
WORKDIR /app

# Copying application files to image
COPY change_line_ending.rb /app/change_line_ending.rb
COPY custom_logger.rb /app/custom_logger.rb
COPY directory_processor.rb /app/directory_processor.rb
COPY file_processor.rb /app/file_processor.rb
COPY Gemfile /app/Gemfile

# Line ending conversion - neseccary if building under Windows
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix * && apt-get --purge remove -y dos2unix && rm -rf /var/lib/apt/lists/*

# Installing application dependencies
RUN gem install bundler && bundler

# Setting entrypoint
ENTRYPOINT ["/app/change_line_ending.rb"]