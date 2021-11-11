FROM alpine:3.4
MAINTAINER Xueshan Feng <sfeng@stanford.edu>
ADD start.sh /start.sh
RUN chmod +x /start.sh
VOLUME ["/shared"]
CMD [ "/start.sh" ]
