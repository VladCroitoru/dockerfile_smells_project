FROM docker:18.03.1
RUN apk --no-cache --update add \
        jq
ADD ./bin /bin
ENTRYPOINT ["entrypoint.sh"]
