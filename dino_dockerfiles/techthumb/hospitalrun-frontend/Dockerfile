FROM  alpine:latest
RUN   apk update
RUN   apk upgrade
RUN   apk add bash            \
              build-base      \
              curl            \
              git             \
              nodejs          \
              openssh-client  \
              python          \
              ruby
RUN   npm install -g npm
RUN   curl -Ls https://github.com/fgrehm/docker-phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz | tar xz -C /
RUN   gem install scss-lint --no-rdoc --no-ri
