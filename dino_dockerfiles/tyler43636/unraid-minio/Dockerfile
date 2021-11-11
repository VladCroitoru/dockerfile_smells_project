FROM minio/minio:latest

MAINTAINER Tyler Payne <tyler43636@gmail.com>

# run script to set uid, gid and permissions
CMD ["minio", "server", "/export"]

HEALTHCHECK CMD curl --fail http://localhost:9000/ || exit 1
