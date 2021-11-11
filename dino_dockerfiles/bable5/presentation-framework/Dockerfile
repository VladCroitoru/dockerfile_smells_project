FROM node:8-slim
LABEL maintainer="Sean L. Mooney <bable4@gmail.com>"

RUN apt-get update
RUN apt-get install -y curl git bzip2

WORKDIR /slidedeck

# Install reveal.js
RUN git clone https://github.com/hakimel/reveal.js.git && \
  cd reveal.js && \
  git checkout 3.7.0 && \
  npm install


FROM node:8-alpine

RUN mkdir -p /slidedeck/slides


RUN addgroup -S slidedeck && \
    adduser -S -g slidedeck slidedeck -h /slidedeck && \
    mkdir -p /slidedeck

COPY --from=0 /slidedeck /slidedeck

RUN ls -l /slidedeck

RUN chown -R  slidedeck:slidedeck /slidedeck

USER slidedeck

EXPOSE 8000
RUN ls -l .

WORKDIR /slidedeck/reveal.js

CMD ["npm", "start"]


