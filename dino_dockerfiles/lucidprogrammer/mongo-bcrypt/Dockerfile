FROM mongo:3.2
MAINTAINER Lucid Programmer <lucidprogrammer@hotmail.com>
# add, just the absolute necessary items alone for the purpose
RUN apt-get update && apt-get install -y curl make g++ python
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g @carsondarling/bcrypt-cli --unsafe-perm
RUN mkdir /mongotemp && chown -R mongodb /mongotemp
