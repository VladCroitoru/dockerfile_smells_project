FROM node:boron

WORKDIR /srv
ADD index.js LICENSE package.json stats.htm stats.js Chart.bundle.min.js /srv/
RUN npm install --production
EXPOSE 8000 8001
CMD [ "nodejs", "index.js" ]