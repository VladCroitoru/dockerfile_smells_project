FROM novemberde/node-pm2

# RUN npm install -g pm2 node-gyp

ENV NODE_ENV production
ENV PORT 80

EXPOSE 80

COPY ./ /src

RUN npm install --prefix /src

CMD ["node", "/src/bin/www"]