FROM node:0.10-slim
ENV app_dir /curvytron
WORKDIR ${app_dir}
ADD . ${app_dir}
RUN apt-get update && apt-get install git python make g++ -y \
  && rm -rf /var/lib/apt/lists/*
RUN npm install gulp -g && npm install bower -g && npm install && bower install --allow-root
RUN gulp
EXPOSE 8080
CMD node bin/curvytron.js
