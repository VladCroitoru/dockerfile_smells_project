FROM python:3.4.3

RUN mkdir /data
RUN pip install awscli==1.7.34

ADD run.sh /run.sh
RUN chmod 755 /run.sh

ENV AWS_ACCESS_KEY_ID **DefineMe**
ENV AWS_SECRET_ACCESS_KEY **DefineMe**
ENV AWS_DEFAULT_REGION us-west-2
ENV S3_SOURCE_BUCKET_NAME my-bucket
ENV S3_TARGET_BUCKET_NAME my-bucket-backup
# Pick one from http://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html
# private public-read public-read-write authenticated-read bucket-owner-read bucket-owner-full-control log-delivery-write
ENV TARGET_FILE_ACL private

CMD ["/run.sh"]