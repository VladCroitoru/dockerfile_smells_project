FROM docker

RUN mkdir ~/.aws/
RUN apk update && \
    apk add py-pip && \
    pip install awscli
    
    
ENV PATH "/root/.local/bin:${PATH}"
