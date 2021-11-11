FROM haproxy:latest

ADD ./haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
ADD ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh

EXPOSE 8388

ENTRYPOINT ["/bin/entrypoint.sh"]
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
