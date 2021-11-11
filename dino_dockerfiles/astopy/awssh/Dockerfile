FROM ruby:2.4-alpine

RUN apk --no-cache add ca-certificates wget openssh
RUN update-ca-certificates

RUN wget -O - https://github.com/junegunn/fzf-bin/releases/download/0.16.5/fzf-0.16.5-linux_386.tgz | \
        tar -xz -C /usr/local/bin

WORKDIR /usr/local/src

COPY Gemfile ./

RUN bundle update
RUN bundle install

COPY awssh ./

ENTRYPOINT [ "/usr/local/src/awssh" ]
