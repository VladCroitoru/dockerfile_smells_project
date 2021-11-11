FROM nginx:stable

ENV TZ=Asia/Shanghai

WORKDIR /app

COPY . .

EXPOSE 80
EXPOSE 443
EXPOSE 8888

ENTRYPOINT ["nginx", "-g", "daemon off;"]

CMD ["-p", "/app", "-c", "/app/config/nginx.conf"]
