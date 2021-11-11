FROM alpine:3.6

RUN apk --no-cache add libqrencode

ENV COMMENT="Replay Code" \
    OTP_TYPE=totp \
    AUTH_FILE=.google_authenticator \
    OUTPUT_FORMAT=ANSI
CMD : ${SECRET=$(head -n 1 "/key/${AUTH_FILE}")}; \
    qrencode -t "${OUTPUT_FORMAT}" "otpauth://${OTP_TYPE}/${COMMENT}?secret=${SECRET}"