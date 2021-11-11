FROM node:14-alpine3.10 as build

WORKDIR /app/
COPY ./package.json /app/

# Adding git to the image to resolve this issue for mysql2 and TypeScript - https://github.com/types/mysql2/issues/30
RUN apk add --no-cache git && \
    npm install && \
    npm install -g ts-node
COPY . /app/
RUN npm run build:prod

FROM node:14-alpine3.10

COPY --from=build /app/ /app/
COPY sshd_config /etc/ssh/

WORKDIR /etc/ssh/
RUN apk add openssh \
    && echo "root:Docker!" | chpasswd \
    && chmod +x /app/init_container.sh \
    && ssh-keygen -A \
    && npm install -g pm2
# Switch back to /app/ to the logic in server.ts on line 16 can properly evaluate
WORKDIR /app/

EXPOSE 4000 2222
ENTRYPOINT [ "/app/init_container.sh" ]
