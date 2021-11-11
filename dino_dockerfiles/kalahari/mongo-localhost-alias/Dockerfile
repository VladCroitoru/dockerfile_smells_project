FROM mongo:3.2
RUN cp /entrypoint.sh /entrypoint.sh.orig \
  && head -2 /entrypoint.sh.orig > /entrypoint.sh \
  && echo '' >> /entrypoint.sh \
  && echo 'if [ ! -z "$LOCALHOST_ALIAS" -a "$(id -u)" = "0" ]; then' >> /entrypoint.sh \
  && echo '        sleep 3 # give hosts time to be writeable' >> /entrypoint.sh \
  && echo '        echo "127.0.0.1 $LOCALHOST_ALIAS" >> /etc/hosts' >> /entrypoint.sh \
  && echo 'fi' >> /entrypoint.sh \
  && tail -n +3 /entrypoint.sh.orig >> /entrypoint.sh \
  && rm /entrypoint.sh.orig
