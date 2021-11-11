###################################################
# TEST.JUSTINDIROSE.COM
# test.justindirose.com config
# An image built off nginx-jekyll with a test site.
###################################################

# Base Image
FROM justindirose/nginx-jekyll

# File Author / Maintainer
MAINTAINER Justin DiRose desk@justindirose.com

# Add virtual host config
COPY nginx/test.justindirose.com /etc/nginx/sites-available/test.justindirose.com
RUN ln -s /etc/nginx/sites-available/test.justindirose.com /etc/nginx/sites-enabled/test.justindirose.com

# Set up Jekyll
RUN mkdir /srv/jekyll
COPY . /srv/jekyll

# Build Jekyll
WORKDIR /srv/jekyll
RUN bundle install
RUN bundle exec jekyll build --source /srv/jekyll --destination /usr/share/nginx/html

# ENV/EXPOSE
EXPOSE 80
