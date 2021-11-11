FROM node:14-alpine

ARG production

ENV INSTALL_PATH /app

RUN npm install pm2@latest -g

COPY package.json yarn.lock /tmp/
RUN cd /tmp && yarn install $(if [[ ! -z $production ]]; then echo "--production"; fi) \ 
  && mkdir -p ${INSTALL_PATH} \
  && cd ${INSTALL_PATH} \
  && cp -R /tmp/node_modules ${INSTALL_PATH} \
  && rm -r /tmp/* && yarn cache clean 
RUN if [[ -z $production ]] ; then wget --no-check-certificate -q -O - https://github.com/eficode/wait-for/releases/download/v2.1.2/wait-for > /tmp/wait-for && chmod a+x /tmp/wait-for; fi

WORKDIR ${INSTALL_PATH}

COPY . .

EXPOSE 3000 5000

CMD ["yarn", "start"]
