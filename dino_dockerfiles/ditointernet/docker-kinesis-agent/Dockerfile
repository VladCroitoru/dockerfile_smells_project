FROM zendesk/amazon-kinesis-agent:latest

ENV CLOUDWATCH_EMIT_METRICS=true \
    AWS_REGION=us-east-1 \
    KINESIS_FILE_PATTERN="/tmp/app.log*" \
    KINESIS_STREAM=stream \
    KINESIS_PARTITION_KEY_OPTION=RANDOM \
    FIREHOSE_FILE_PATTERN="/tmp/app.log*" \
    FIREHOSE_DELIVERY_STREAM=stream

COPY write_config.sh write_config.sh

CMD ./write_config.sh && /usr/bin/start-aws-kinesis-agent -L $LOG_LEVEL -l /dev/stdout
