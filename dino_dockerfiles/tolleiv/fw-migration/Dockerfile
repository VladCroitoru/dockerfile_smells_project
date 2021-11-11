FROM golang:onbuild
ENV PORT=9000
EXPOSE 9000
RUN echo "db:\n  name: /data/app.db" > config/database.yml
VOLUME /data