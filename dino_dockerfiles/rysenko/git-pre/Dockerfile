FROM node:slim
COPY . .
RUN npm install
EXPOSE  8000
CMD ["./node_modules/.bin/grunt", "serve"]
