FROM golang
RUN go get github.com/seanmclane/goatnickels
ENV CONFIG=""
ENV KEYSTORE=""
ENV USER=""
EXPOSE 3000
RUN goatnickels -init-config y
RUN goatnickels -generate-acct y -save y
RUN goatnickels -genesis y
COPY ${CONFIG} /${USER}/.goatnickels/config.json
COPY ${KEYSTORE} /${USER}/.goatnickels/keystore.json
CMD ["goatnickels", "-serve", "y"]