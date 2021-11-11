FROM alpine:latest

ADD cultd /usr/local/bin/
ADD cultctl /usr/local/bin/

ARG CULT_IMG_VER
ENV CULT_IMG_VER ${CULT_IMG_VER:-v0.13}
RUN echo $CULT_IMG_VER

# Define default command.
CMD ["/usr/local/bin/cultd"]
