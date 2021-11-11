FROM debian:stretch

ENV STORAGE_PATH /mnt/storage
ENV TEST_FILE_NAME a672b70b-75a3-4a60-bad8-1ed2b9729854

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]