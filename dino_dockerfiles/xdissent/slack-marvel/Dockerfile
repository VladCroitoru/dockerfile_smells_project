FROM dockerfile/nodejs

MAINTAINER Greg Thornton <xdissent@me.com>

WORKDIR /slack-marvel

ADD . /slack-marvel

RUN rm -rf node_modules

RUN npm install

EXPOSE 80
 
CMD ["node_modules/.bin/coffee", "app.coffee"]