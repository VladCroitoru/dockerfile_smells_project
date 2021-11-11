FROM node:6.9.5
RUN apt-get update -y &&\
    apt-get install -y libgtk2.0-0 libgconf-2-4 \
    libasound2 libxtst6 libxss1 libnss3 xvfb
RUN groupadd -r electron && useradd -m -r -g electron electron
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app
COPY package.json ./package.json
COPY npm-shrinkwrap.json ./npm-shrinkwrap.json
RUN npm install
COPY ./entrypoint.sh ./
RUN chown -R electron:electron /usr/src/app/ && chmod +x entrypoint.sh
USER electron
ENTRYPOINT ["./entrypoint.sh"]

