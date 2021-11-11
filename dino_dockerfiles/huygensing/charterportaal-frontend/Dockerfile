FROM node:6.2.2-onbuild

RUN npm run build

EXPOSE 3001
EXPOSE 8080
EXPOSE 80

CMD ./scripts/server.js 80
