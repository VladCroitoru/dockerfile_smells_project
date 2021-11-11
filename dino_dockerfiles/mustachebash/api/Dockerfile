FROM node:16.11-alpine
RUN mkdir -p /mustachebash
WORKDIR /mustachebash
COPY package.json package-lock.json ticket-logo.png ./
RUN npm install --production --no-optional && \
	npm cache clean --force

COPY lib lib
EXPOSE 4000
CMD npm start
