FROM alpine
ARG MIRROR_HOST=dl-cdn.alpinelinux.org
ARG MIRROR_SCHEMA=http
RUN sed -i -re "s/http/$MIRROR_SCHEMA/g;s/dl-cdn.alpinelinux.org/$MIRROR_HOST/g" /etc/apk/repositories
RUN apk add -U --no-cache cloc
ENTRYPOINT ["cloc"]
CMD ["--version"]
