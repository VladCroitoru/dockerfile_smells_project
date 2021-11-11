FROM bash:5

RUN apk add -q --no-cache \
  ansible \
  # extensions that are needed in some playbooks
  curl rsync py-netaddr \
  && rm -f /tmp/* /etc/apk/cache/* \
  # enable color prompt
  && mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh
