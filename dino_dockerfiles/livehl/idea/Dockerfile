FROM progrium/busybox

RUN mkdir -p /app
WORKDIR /app
COPY ./server /app/
EXPOSE 80

CMD /app/server -p 80
