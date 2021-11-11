# Base image define : builder stage - 다음 from까지
FROM node:14-alpine as builder

WORKDIR '/usr/src/app'
# 종속성만 먼저 build : cache 사용
COPY package.json ./
RUN npm install

# 변경된 소스 적용
COPY ./ ./
RUN npm run build

# 시작시 실행될 명령어
#CMD ["node", "app.jsx"]

FROM nginx as runner
#COPY default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80 443
COPY --from=builder /usr/src/app/build /usr/share/nginx/html