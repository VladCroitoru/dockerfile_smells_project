FROM debian:jessie


COPY ./app/public /app/public
copy ./app/src/main /app/main
RUN chmod +x /app/main;

WORKDIR /app


CMD /app/main