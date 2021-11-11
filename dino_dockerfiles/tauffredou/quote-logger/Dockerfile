FROM alpine:3.6
RUN apk add --no-cache curl 
CMD echo start; while sleep 5; do curl -s  -X POST 'http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=text'; echo;  done

