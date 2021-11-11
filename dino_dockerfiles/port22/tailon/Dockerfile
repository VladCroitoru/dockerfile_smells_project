FROM python:alpine

RUN pip install tailon                \
&&  apk add -U --no-cache grep gawk   \
&&  rm -f /usr/bin/awk /bin/grep      \
&&  ln -s /usr/bin/gawk /usr/bin/awk  \
&&  ln -s /usr/bin/grep /bin/grep

CMD /usr/local/bin/tailon -b 0.0.0.0:80 -t 9999 -f /log
