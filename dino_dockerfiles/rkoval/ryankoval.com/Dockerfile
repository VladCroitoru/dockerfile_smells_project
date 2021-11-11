FROM node:10.1.0-alpine as webpack
COPY *.json ./
RUN npm install && npm cache clean --force
VOLUME ['./node_modules']
COPY static ./static
COPY *.js ./
COPY src ./src
RUN npm run build

FROM alpeware/chrome-headless-stable:ver-63.0.3239.132 as pdf
WORKDIR /tmp/dist
COPY --from=webpack ./dist/. .
RUN nohup python3 -m http.server 1234 & \
    sleep 2 && \
    google-chrome-stable \
      --headless \
      --no-sandbox \
      --disable-gpu \
      --print-to-pdf \
      http://localhost:1234/resume.html
RUN chmod +r output.pdf

FROM nginx:1.13.12-alpine
EXPOSE 80
COPY ./docker_root /
COPY --from=webpack ./dist/. /usr/share/nginx/html
COPY --from=pdf /tmp/dist/output.pdf /usr/share/nginx/html/resume.pdf
