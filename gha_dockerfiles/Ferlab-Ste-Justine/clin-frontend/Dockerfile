FROM node:14.15.1 as builder
ADD . /code
WORKDIR /code
RUN npm install -g pnpm
RUN pnpm install
RUN pnpm build

FROM nginx:1 as server

COPY --from=builder /code/client/build /usr/share/nginx/html/
COPY --from=builder /code/client/build /var/www/html/

COPY static.conf /etc/nginx/conf.d/default.conf

COPY entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
