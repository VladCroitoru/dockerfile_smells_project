FROM brogency/react-baobab-isomorphic-stub:2.1.1
WORKDIR /app
ADD package.json ./package.json
RUN npm i
ADD . /app/user/
WORKDIR /app/user/
RUN npm run build
