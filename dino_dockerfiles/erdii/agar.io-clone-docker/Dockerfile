FROM erdii/nodejs-0.10-buildtools

RUN mkdir /wd
WORKDIR /wd

RUN git clone https://github.com/huytd/agar.io-clone
WORKDIR /wd/agar.io-clone

RUN npm install

CMD [ "npm", "start" ]


