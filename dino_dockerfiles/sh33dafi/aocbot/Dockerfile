FROM mhart/alpine-node:6
ADD . .
RUN npm run build
CMD ["node", "dist/build.js"]
