FROM node:4.4.5
MAINTAINER tomo3110
RUN git clone --depth 1 https://github.com/tomo3110/minutes-sync.git
WORKDIR minutes-sync
ENV PORT=3306
RUN npm install
CMD ["npm", "start"]
