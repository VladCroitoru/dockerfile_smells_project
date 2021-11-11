# image to test SCRAM-SHA-1 auth
# database: admin
# username: admin
# password: admin
FROM mongo:3.2

# designate a new data directory (the original one is volumized, no data is persisted)
ENV MONGO_DBPATH /data/test-db
RUN mkdir -p ${MONGO_DBPATH} && chown -R mongodb:mongodb ${MONGO_DBPATH}

COPY set-password.sh /
RUN /set-password.sh

RUN chown -R mongodb:mongodb ${MONGO_DBPATH}

# docker won't expand MONGO_DBPATH here, so have to use the value itself
CMD ["mongod", "--auth", "--dbpath=/data/test-db"]
