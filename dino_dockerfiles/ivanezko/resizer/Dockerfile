FROM h2non/imaginary:latest
ENV PORT "9000"
COPY empty.jpg .
CMD ["-enable-url-source", "-enable-placeholder", "-placeholder", "empty.jpg", "-http-read-timeout" ,"3", "-concurrency", "20", "-allowed-origins", "https://mywebsite.com"]
