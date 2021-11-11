FROM mkieboom/mapr-jumpbox-base

# Set the VNC password
ENV VNC_PW=maprbootcamp

# Switch to root user
USER root

# Install ssh client, nfs libraries, mousepad (graphical text editor), xdg-utils (to set default apps)
RUN yum install -y git openssh-clients nfs-utils nfs-utils-lib mousepad xdg-utils && \
    yum clean all && \
    rm -rf /var/cache/yum

########################################################################
# Set default applications for hyperlinks
########################################################################
RUN sed -ie "s|firefox.desktop|chromium-browser.desktop|g" /usr/share/applications/mimeapps.list

#########################################################################
# MapR Jumpbox - add basics (background image)
#########################################################################

# Add the MapR desktop background picture
ADD desktop_background_image/mapr_background.png /headless/.config/
ADD desktop_background_image/xfce4-desktop.xml /headless/.config/xfce4/xfconf/xfce-perchannel-xml

# Add a launch script creating the mapr group and user
ADD launch-jumpbox.sh /launch-jumpbox.sh
RUN sudo -E chmod +x /launch-jumpbox.sh

# Add the desktop hyperlinks
ADD desktop_shortcuts/*.desktop /headless/Desktop/bootcamp-hyperlinks/

# Make all hyperlinks executable
RUN chmod +x  /headless/Desktop/bootcamp-hyperlinks/*.desktop
RUN chmod +x /headless/Desktop/*.desktop

# Mount the MapR cluster in /mapr
ADD /mount-maprfs-script.sh /
RUN chmod +x /mount-maprfs-script.sh
RUN sudo mkdir /mapr

#########################################################################
# MapR Jumpbox - bootcamp files
#########################################################################

RUN git clone https://github.com/mkieboom/mapr-ansible-playbooks

# Place the example images on the desktop
RUN mv mapr-ansible-playbooks/bootcamp-dataset/example_images /headless/Desktop/

# Place the scripts, streamsets pipelines and DSR notebook also on the desktop
RUN mv mapr-ansible-playbooks/bootcamp-dataset /headless/Desktop/

#########################################################################
# MapR Jumpbox - launch
#########################################################################

ADD /mount-maprfs-launch.sh /headless/Desktop/
RUN chmod +x /headless/Desktop/*.sh

# Run the launch script and use a tail to keep the container running
CMD sudo -E /launch-jumpbox.sh && tail -f /headless/wm.log
