FROM ubuntu:20.04

# the postconf settings below do ...
# - limit to 1000 messages per 60 second
# - only listen for IPv4
# - log to stdout
# - messages 10mb max
# - require a HELO when connecting
# - only allow relaying by email addresses listed in the /etc/postfix/sender_access file or from our permitted networks

RUN apt-get update && apt-get install -y postfix dnsutils && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    postconf -e "smtpd_client_message_rate_limit=1000" && \
    postconf -e "anvil_rate_time_unit=60s" && \
    postconf -e "inet_protocols=ipv4" && \
    postconf -e "maillog_file=/dev/stdout" && \
    postconf -e "message_size_limit=10240000" && \
    postconf -e "smtpd_delay_reject=no" && \
    postconf -e "smtpd_helo_required=yes" && \
    postconf -e "local_transport=error:not allowed" && \
    postconf -e "smtpd_relay_restrictions=check_sender_access hash:/etc/postfix/sender_access reject_unlisted_sender permit_mynetworks permit_sasl_authenticated defer_unauth_destination" && \
    postconf -e "smtpd_sender_restrictions=check_sender_access hash:/etc/postfix/sender_access reject_unlisted_sender" && \
    postconf -e "relay_domains="

COPY docker-entrypoint.sh /docker-entrypoint.sh
ENTRYPOINT [ "/docker-entrypoint.sh" ]

CMD ["postfix", "start-fg"]
