FROM linuxserver/swag

RUN apk --no-cache add \
        mailx \
        ssmtp && \
    ln -sf /config/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf && \
    ln -sf /config/ssmtp/revaliases /etc/ssmtp/revaliases
