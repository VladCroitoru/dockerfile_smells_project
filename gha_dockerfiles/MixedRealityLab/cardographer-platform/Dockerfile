FROM node:alpine
RUN mkdir /app
WORKDIR /app
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install
COPY *.config.js *.config.cjs tsconfig.json .npmrc /app/
COPY ./src/ /app/src
COPY ./static/ /app/static
ENV NODE_ENV=production
RUN npm run build
EXPOSE 3000
VOLUME /app/static/uploads

#CMD ["npm", "run", "preview"]
CMD ["node", "build"]
#CMD ["/bin/sh"]
