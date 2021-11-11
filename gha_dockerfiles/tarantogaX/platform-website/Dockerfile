FROM node
RUN mkdir camps
WORKDIR camps

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install
COPY . ./

RUN npm run build

EXPOSE 3000

CMD npm run start