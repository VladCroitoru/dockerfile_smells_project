FROM node:12.0.0

WORKDIR /app
COPY .env-cmdrc /app
COPY package*.json /app/
COPY tsconfig.json /app
COPY src /app/src/
#RUN ls -a
#RUN npm install -g typescript
#RUN npm install -g tsc
RUN npm install
#RUN npm run remove-dist
RUN npm run build
CMD npm run start-prod
EXPOSE 4500