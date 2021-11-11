FROM gallna/grunt-devtools
MAINTAINER Tomasz Jonik <tomasz@hurricane.works>

# Install Sass
RUN apt-get update && apt-get install -y --force-yes rubygems
RUN gem install sass

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["grunt-devtools"]
