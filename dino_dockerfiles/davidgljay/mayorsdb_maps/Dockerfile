FROM node
MAINTAINER "David Jay <davidgljay@gmail.com>"
LABEL updated_at = "2015-1-20" version = .03
LABEL description = "A service for mapping mayoral press releases for display."
RUN apt-get update
COPY ./ /home/mayorsdb
WORKDIR /home/mayorsdb
RUN npm install
CMD node index