FROM node:12.22-alpine
RUN npx create-react-app stamp
WORKDIR /stamp
ADD https://github.com/wildme/stamp/tarball/v0.5  /tmp
RUN tar xzf /tmp/v0.5 --strip-components=1 -C /stamp
RUN npm install --silent
EXPOSE 3001 3000
CMD ["npm", "start"]
