FROM python:3-slim

ADD ./blockfinder /usr/src/app/blockfinder
RUN mkdir /usr/src/app/.blockfinder \
  && ./usr/src/app/blockfinder -i --cache-dir /usr/src/app/.blockfinder/

ENTRYPOINT ["./usr/src/app/blockfinder"]
