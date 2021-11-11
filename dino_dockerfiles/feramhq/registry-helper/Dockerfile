FROM alpine:3.7

# Install AWS CLI and Docker
RUN apk --no-cache add \
        python \
        py-pip \
        docker \
        && \
    pip install --upgrade awscli==1.14.5 && \
    apk -v --purge del py-pip
RUN docker -v
RUN aws --version

COPY app.sh app.sh

CMD ./app.sh

# Check if file was modified in the last 7h (420 minutes)
HEALTHCHECK --interval=60s \
  CMD [ "/usr/bin/find", "/heartbeat", "-mmin", "+420", "-exec", "false", "{}", "+" ]
