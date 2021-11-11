FROM node:6.7.0

ENV NODE_MEM 2056

ADD bin bin
ADD package.json package.json
RUN npm install
CMD node --max_old_space_size=${NODE_MEM} bin/generate-env /tmp/output_data
