#
# Jekyll - Ubuntu
#

# Pull base image.
FROM ubuntu
# Install Ruby + gems
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y git git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 
RUN apt-get install -y libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties ruby ruby-dev make

# Install Nodejs
RUN apt-get install -y nodejs

# Install Jekyll
RUN gem install jekyll --no-rdoc --no-ri

# Attach volumes.
RUN mkdir -p /usr/share/nginx/html
VOLUME /usr/share/nginx/html

# Build jekyll site
CMD git clone https://github.com/firefightio/blog-firefightio.git && jekyll build --source /blog-firefightio --destination /usr/share/nginx/html && chmod 755 /usr/share/nginx/html

# Debug command.
#CMD ["/bin/bash"]
