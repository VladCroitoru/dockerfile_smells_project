FROM node:5.7.1

ADD . .
RUN npm install
CMD node --harmony_destructuring --max_old_space_size=2056 bin/generate-env.js
