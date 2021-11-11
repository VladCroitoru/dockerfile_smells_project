FROM nginx:alpine
RUN apk --update upgrade && \
    apk add --no-cache \
      curl && \
      rm -rf /var/cache/apk/*
ADD ./src/start.sh /start.sh 
CMD /start.sh ${chaos_sleep}
