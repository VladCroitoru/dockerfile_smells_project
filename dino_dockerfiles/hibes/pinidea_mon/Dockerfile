FROM hibes/debian-node-docker

ENV LOGFILE=/pinidea_mon.log

LABEL org.freenas.interactive="false"                                                   \
      org.freenas.version="1.01"                                                        \
      org.freenas.upgradeable="false"                                                   \
      org.freenas.expose-ports-at-host="true"                                           \
      org.freenas.autostart="true"                                                      \
      org.freenas.settings="[                                                           \
        {                                                                               \
          \"env\": \"destinationEmail\",                                                \
          \"descr\": \"The e-mail to send updates to\",                                 \
          \"optional\": false                                                           \
        },                                                                              \
        {                                                                               \
          \"env\": \"freq\",                                                            \
          \"descr\": \"The frequency with which the pinidea website should be polled\", \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"emailSubject\",                                                    \
          \"descr\": \"The subject line to be used when sending e-mails\",              \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"periodicEmailSubject\",                                            \
          \"descr\": \"The subject line to be used when sending periodic e-mails\",     \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"periodicEmailFreq\",                                               \
          \"descr\": \"The frequency with which the periodic e-mails should go out\",   \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"sourceEmail\",                                                     \
          \"descr\": \"The e-mail to use as the From address for all e-mails\",         \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"sourceName\",                                                      \
          \"descr\": \"The name to use in the From address for all e-mails\",           \
          \"optional\": true                                                            \
        },                                                                              \
        {                                                                               \
          \"env\": \"emailUser\",                                                       \
          \"descr\": \"The e-mail address to use to log in and send e-mails\",          \
          \"optional\": false                                                           \
        },                                                                              \
        {                                                                               \
          \"env\": \"emailPass\",                                                       \
          \"descr\": \"The password to use to log in to that e-mail address\",          \
          \"optional\": false                                                           \
        },                                                                              \
        {                                                                               \
          \"env\": \"emailTransportService\",                                           \
          \"descr\": \"The transport service to use (e.g. gmail) -- see nodemailer\",   \
          \"optional\": true                                                            \
        }                                                                               \
      ]"

COPY . ./

CMD npm run start | tee -a ${LOGFILE}
