FROM python:2.7-alpine

RUN apk --no-cache add --virtual=.build-dep \
      build-base \
    && apk --no-cache add bash libzmq \
    && apk del .build-dep

# COPY STUFF
COPY tcollector.py entrypoint.sh /tcollector/
COPY collectors/ /tcollector/collectors/
#
RUN chmod +x /tcollector/entrypoint.sh

# Start 
ENTRYPOINT ["/tcollector/entrypoint.sh"] 
