FROM xueshanf/awscli

LABEL maintainer "grrywlsn"

CMD aws s3 cp $(echo $SOURCE_DIR) s3://$(echo $S3_DIR)/$(date '+%Y-%m')/$(date '+%d')/$(date '+%H:%M')/ --recursive
