FROM node:latest

ENV NODE_ENV production
ENV PORT 3000

EXPOSE 3000

COPY package.json /app/
WORKDIR /app

# improve npm install speed
RUN npm set progress=false
RUN npm install

COPY . /app/

ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["npm", "run", "start"]
