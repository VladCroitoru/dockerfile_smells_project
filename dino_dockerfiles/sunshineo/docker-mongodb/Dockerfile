FROM mongo:3.2.9

COPY ./docker-mongo-entrypoint.sh /docker-mongo-entrypoint.sh

ENTRYPOINT ["/docker-mongo-entrypoint.sh"]
CMD ["mongod"]