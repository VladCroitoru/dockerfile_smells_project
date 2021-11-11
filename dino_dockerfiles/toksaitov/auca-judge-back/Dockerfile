FROM node:4.4.4-slim

EXPOSE 7070
WORKDIR /auca-judge-back

COPY package.json /auca-judge-back
RUN apt-get update                                           && \
    apt-get install --assume-yes git --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*                              && \
    npm install                                              && \
    apt-get purge --assume-yes --auto-remove git

COPY . /auca-judge-back

CMD ["npm", "start"]
