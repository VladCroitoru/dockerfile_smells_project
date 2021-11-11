FROM mhart/alpine-node:latest
RUN apk add --no-cache git
RUN npm install -g s3rver@3.6.1
RUN npm install aws-sdk
WORKDIR /
COPY CORS.xml /CORS.xml
EXPOSE 5000
CMD s3rver -a 0.0.0.0 --port 5000 \
    --allow-mismatched-signatures \
    --no-vhost-buckets \
    --directory /tmp \
    --configure-bucket "$S3_BUCKET_NAME" /CORS.xml $S3RVER_EXTRA_ARGS
