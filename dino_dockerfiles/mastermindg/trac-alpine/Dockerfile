FROM alpine

ENV projectname="myproject"
ENV user="admin"
ENV password="admin"

RUN apk add --no-cache python bash trac

RUN mkdir /trac

COPY run.sh /

CMD /run.sh
