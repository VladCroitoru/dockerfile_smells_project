FROM hurricane/dockergui:x11rdp1.3
MAINTAINER johnodon <johnodon68@gmail.com>

# User/Group Id gui app will be executed as
ENV USER_ID="99" GROUP_ID="100" APP_NAME="Inkscape" TERM="xterm" WIDTH="1280" HEIGHT="720"

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

# Install Inkscape
ADD ./files /files/
RUN chmod +x /files/install.sh && sleep 1 && /files/install.sh && rm -r /files

VOLUME ["/nobody/.config/inkscape"]
EXPOSE 3389 8080
