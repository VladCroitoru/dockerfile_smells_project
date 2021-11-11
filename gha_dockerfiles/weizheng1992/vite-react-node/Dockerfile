
FROM node:14-alpine AS BUILD_IMAGE

LABEL name "react-back"
LABEL version = "1.0"

COPY . /app

WORKDIR /app

RUN yarn install 

# 暴露容器端口
EXPOSE 8099

# 启动node应用
CMD ["yarn","prod"]
