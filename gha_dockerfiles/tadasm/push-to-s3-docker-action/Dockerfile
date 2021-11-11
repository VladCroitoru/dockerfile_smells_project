# Container image that runs your code
FROM amazon/aws-cli

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

COPY aws-s3-sync.sh /aws-s3-sync.sh

COPY aws-cloudfront-cache-invalidate.sh /aws-cloudfront-cache-invalidate.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
