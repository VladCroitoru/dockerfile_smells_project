FROM stilliard/pure-ftpd:hardened

RUN cd /etc/pure-ftpd/conf/ && \
        echo "yes" | tee AllowUserFXP && \
        echo "yes" | tee NATmode