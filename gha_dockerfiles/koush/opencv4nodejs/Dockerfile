FROM koush/node-opencv

WORKDIR /
COPY . opencv4nodejs

ARG NODE_PRE_GYP_GITHUB_TOKEN

WORKDIR /opencv4nodejs
RUN npm install
RUN npm run build
RUN npm run node-pre-gyp-publish
