FROM alpine
MAINTAINER Robin N. Mai <robin.nepomuk.mai@me.com>
RUN apk update && apk upgrade
RUN apk add bash
RUN apk add nodejs
RUN npm install -g newman@beta
RUN mkdir /home/newman
RUN chmod 777 /home/newman

EXPOSE 80 443
CMD ["newman"]
