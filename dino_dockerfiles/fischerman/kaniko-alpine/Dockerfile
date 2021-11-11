FROM gcr.io/kaniko-project/executor@sha256:2041c6969749e99cf1c66ad24437631f31ebe0965fd44d5852640db3e0b48089

ADD entrypoint.sh /kaniko/
#RUN chmod +x /kaniko/entrypoint.sh

ENTRYPOINT [ "/kaniko/entrypoint.sh" ]