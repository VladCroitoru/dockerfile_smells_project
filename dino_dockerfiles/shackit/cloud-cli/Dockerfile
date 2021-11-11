FROM python:2.7.14-alpine as cli-base

RUN apk --no-cache add --update gcc musl-dev \
    && pip install awscli==1.14.44 \
    && pip install aliyuncli==2.1.5 \
    && pip install aliyun-python-sdk-ecs==4.6.3

FROM python:2.7.14-alpine
COPY --from=cli-base /root/.cache /root/.cache
RUN pip install awscli==1.14.44 \
    && pip install aliyuncli==2.1.5 \
    && pip install aliyun-python-sdk-ecs==4.6.3 \
    && rm -rf /root/.cache
