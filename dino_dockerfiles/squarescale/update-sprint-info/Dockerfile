FROM ruby:2-alpine
MAINTAINER SquareScale Engineering <engineering@squarescale.com>
LABEL maintainer "SquareScale Engineering <engineering@squarescale.com>"
LABEL name "Update agile board"
LABEL version "0.1.0"
ENV REFRESHED_AT 2017-05-18

RUN gem install octokit

COPY update_sprint_info.rb /usr/src/app/update_sprint_info.rb

CMD ["ruby", "/usr/src/app/update_sprint_info.rb"]

