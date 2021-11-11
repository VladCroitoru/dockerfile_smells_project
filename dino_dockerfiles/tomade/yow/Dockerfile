FROM python:alpine
RUN apk add --no-cache tini
USER nobody
COPY . .
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["python", "yow.py"]
EXPOSE 8080
