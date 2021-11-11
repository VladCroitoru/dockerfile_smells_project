# 使用 node 镜像
FROM node:16-alpine

# 准备工作目录
RUN mkdir -p /app/client
WORKDIR /app/client

# 复制 package.json
COPY package*.json /app/client/

# 安装依赖
# RUN npm install

# 复制文件
COPY . /app/client

EXPOSE  3000

# 启动服务
CMD ["npm", "run", "start"]