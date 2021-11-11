FROM debian:buster-slim
WORKDIR /
ADD ./artifactor /

RUN adduser -u 1000 --disabled-password --no-create-home --gecos "" app_user
RUN chmod +x ./artifactor
RUN chown 1000 ./artifactor

USER app_user

CMD ["./artifactor"]