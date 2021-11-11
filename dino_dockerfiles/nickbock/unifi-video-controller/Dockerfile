FROM pducharme/unifi-video-controller:latest
LABEL org.freenas.interactive="false" \
      org.freenas.version="3.6.2" \
      org.freenas.upgradeable="false" \
      org.freenas.expose-ports-at-host="true" \
      org.freenas.autostart="true" \
      org.freenas.web-ui-protocol="https" \
      org.freenas.web-ui-port="7443" \
      org.freenas.web-ui-path="manage" \
      org.freenas.port-mappings="7443:7443/tcp,7445:7445/tcp,7446:7446/tcp,7447:7447/tcp,7080:7080/tcp,6666:6666/tcp" \
      org.freenas.volumes="[                        \
          {                             \
              \"name\": \"/var/lib/unifi-video\",                    \
              \"descr\": \"UniFi Configuration Data\"           \
          },    \
          {                             \
              \"name\": \"/var/log/unifi-video\",                    \
              \"descr\": \"UniFi Logs\"           \
          },    \
                            \
          {                             \
              \"name\": \"/usr/lib/unifi-video/data/videos\",                    \
              \"descr\": \"Video files\"          \
          }                             \
      ]"                                \
      org.freenas.settings="[                       \
          {                             \
              \"env\": \"TZ\",                      \
              \"descr\": \"Timezone - eg Europe/London\",       \
              \"optional\": true                    \
          }                             \
      ]"
