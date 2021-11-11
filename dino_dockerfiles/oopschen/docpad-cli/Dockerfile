# DocPad Dockerfile
FROM oopschen/alpine-nodejs:latest
MAINTAINER Ray Chen <linxray@gmail.com>

# DocPad authentication.
RUN echo -e "{\n  subscribed: false\n  subscribeTryAgain: false\n  tos: true\n  identified: true\n}" > ~/.docpad.cson

# Install DocPad globally.
RUN npm install -g docpad

# Set up the application directory.

VOLUME ["/app"]
WORKDIR /app


# Expose the default DocPad port.

EXPOSE 9778


# Launch DocPad when the container stars, passing through any arguments.
CMD ["-"]
ENTRYPOINT ["docpad"]
