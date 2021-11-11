FROM node
MAINTAINER "David Jay <davidgljay@gmail.com>"
LABEL updated_at = "2015-1-14" version = .01
LABEL description = "A service for adding topic tags to mayoral press releases."
RUN apt-get update
COPY ./ /home/mayorsdb
WORKDIR /home/mayorsdb
RUN npm install
CMD node index

