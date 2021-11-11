FROM alpine
RUN apk add --no-cache \
  bash \
  iproute2 
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]