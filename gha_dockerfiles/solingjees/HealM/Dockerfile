FROM node:14.17.0 as build-stage

LABEL maintainer=1600346867@qq.com

WORKDIR /app

COPY . .

RUN npm install --registry=https://registry.npm.taobao.org
RUN npm run build

FROM nginx:stable-alpine as production-stage
# 将build-stage:/app/dist->production-stage:/usr/share/nginx/html
COPY --from=build-stage /app/dist /usr/share/nginx/html
# 暴露80端口，方便镜像映射
EXPOSE 80
# container运行时执行命令，保证nginx container不挂
CMD ["nginx", "-g", "daemon off;"]