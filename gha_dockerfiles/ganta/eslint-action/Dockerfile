FROM node:14-buster-slim

RUN npm config set progress false

COPY lib /action/lib

ENTRYPOINT ["/action/lib/linter.sh"]
