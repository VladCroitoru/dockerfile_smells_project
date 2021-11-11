FROM openjdk:8-jdk

# Cantaloupe docker starter script

ENV CANTALOUPE_VERSION 4.0.2

# Update packages and install tools 
RUN apt-get update && apt-get install -y --no-install-recommends \
	wget git gcc g++ unzip make pkg-config

# Install imaging tools
RUN apt-get install -y liblcms2-dev  libtiff-dev libpng-dev libz-dev libopenjp2-tools

# run non priviledged
RUN groupadd -f www-data && useradd -d /home -g www-data -s /sbin/false cantaloupe

#
# Cantaloupe
#
WORKDIR /tmp
RUN curl -OL https://github.com/medusa-project/cantaloupe/releases/download/v$CANTALOUPE_VERSION/Cantaloupe-$CANTALOUPE_VERSION.zip \
 && mkdir -p /usr/local/ \
 && cd /usr/local \
 && unzip /tmp/Cantaloupe-$CANTALOUPE_VERSION.zip \
 && ln -s cantaloupe-$CANTALOUPE_VERSION cantaloupe \
 && rm -rf /tmp/Cantaloupe-$CANTALOUPE_VERSION \
 && rm /tmp/Cantaloupe-$CANTALOUPE_VERSION.zip

# Ruby dependencies
ENV GEMSDIR /home/.gem/jruby/2.3.0
RUN apt-get install -y rubygems
RUN gem install -i $GEMSDIR jwt aws-sdk 

# Configuration and log directories
COPY cantaloupe.properties /etc/cantaloupe.properties 
RUN mkdir -p /var/log/cantaloupe \
 && mkdir -p /var/cache/cantaloupe \
 && chown -R cantaloupe /var/log/cantaloupe \
 && chown -R cantaloupe /var/cache/cantaloupe \
 && chown cantaloupe /etc/cantaloupe.properties

# Delegate script and dependencies
COPY delegates.rb /etc/delegates.rb
COPY keyfile-pub.pem /etc/keyfile-pub.pem
EXPOSE 8182

USER cantaloupe 
WORKDIR /home
CMD ["sh", "-c", "java -Dcantaloupe.config=/etc/cantaloupe.properties -Xmx8000m -jar /usr/local/cantaloupe/cantaloupe-$CANTALOUPE_VERSION.war"]
