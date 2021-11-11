FROM wernight/duplicity:latest

USER root

RUN apk update && apk upgrade && \
    apk add --no-cache python && \
		apk add --no-cache python-dev && \
		apk add --no-cache py-pip && \
		apk add --no-cache build-base && \
		apk add --no-cache openssl-dev && \
		apk add --no-cache libffi-dev
		
RUN pip install --no-cache-dir azure