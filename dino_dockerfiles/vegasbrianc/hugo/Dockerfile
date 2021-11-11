FROM alpine:3.2

# Install software
RUN apk add --update go && rm -rf /var/cache/apk/*

# Download and install hugo
ENV HUGO_VERSION 0.14
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64

ADD https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz /usr/local/
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \
    && ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \
    && rm /usr/local/${HUGO_BINARY}.tar.gz

# Create working directory
RUN mkdir /usr/share/blog
WORKDIR /usr/share/blog

# Automatically build site
ONBUILD ADD site /usr/share/blog
RUN hugo new site /usr/share/blog

# Install Hugo Base theme and cleanup afterwards
ADD https://github.com/crakjie/hugo-base-theme/archive/master.zip /usr/share/blog/

RUN unzip /usr/share/blog/master.zip
RUN cp -R /usr/share/blog/hugo-base-theme-master/* /usr/share/blog
RUN rm -R /usr/share/blog/hugo-base-theme-master
RUN rm /usr/share/blog/master.zip

# Edit the Hugo Config
RUN sed -i -e"s/baseurl\s*=\s*\"http:\/\/gohugo.io\"/baseurl = \"http:\/\/localhost\"/" /usr/share/blog/config.toml

# By default, serve site
CMD hugo server -baseUrl "http://localhost/" --watch --port=80 --appendPort=false --bind=0.0.0.0

EXPOSE 80
