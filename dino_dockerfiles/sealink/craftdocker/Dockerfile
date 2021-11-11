FROM sealink/phpdocker:7.0.12

# Set craft version
ENV CRAFTURL 'https://download.craftcdn.com/craft/2.6/2.6.2973/Craft-2.6.2973.zip'

WORKDIR /app/

# Download the latest Craft, save as craft.zip in current folder and extract
# just the craft directory and index out of the archive, quietly
RUN \
  wget $CRAFTURL -O/app/craft.zip && \
  unzip -qqo /app/craft.zip 'craft/*' public/index.php && \
  rm /app/craft.zip && \
  mkdir public/admin && \
  cp -R craft/app/resources public/admin

# create craft version
RUN echo $(egrep '(CRAFT_VERSION|CRAFT_BUILD)' /app/craft/app/Info.php | awk '{print $2}' | sed s@[^0-9\.]@@g) | tee public/craftversion.txt

# remove default template files
RUN rm -rf /app/craft/templates/*

# Add pansophy support for deploying configuration files
RUN \
  apt-get update && \
  apt-get -y install libreadline-dev && \
  apt-get clean
RUN git clone https://github.com/rbenv/ruby-build.git /ruby-build
RUN /ruby-build/install.sh
RUN ruby-build 2.3.1 /ruby-2.3.1
ENV PATH /ruby-2.3.1/bin:$PATH
RUN gem install pansophy mime-types --no-ri --no-rdoc
COPY Rakefile /app/

# add default config
ADD ./config /app/craft/config

RUN chown -Rf nginx:nginx /app

EXPOSE 80
