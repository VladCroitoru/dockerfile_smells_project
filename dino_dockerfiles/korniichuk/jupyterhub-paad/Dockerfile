# Name: korniichuk/jupyterhub-paad
# Short Description: JupyterHub for the PAAD project
# Full Description: The korniichuk/jupyterhub Docker image for the PAAD project.
# Version: 0.3a1

FROM korniichuk/jupyterhub:0.1

MAINTAINER Ruslan Korniichuk <ruslan.korniichuk@gmail.com>

USER root

# Retrieve new lists of packages
ENV REFRESHED_PACKAGES_AT 2016–01–20
RUN apt-get -qq update # -qq -- no output except for errors

# Install emacs, mc, nano, screen, ssh, sshfs, vim, wget
RUN apt-get install -y emacs emacs-goodies-el emacs24-el mc nano screen ssh sshfs vim wget && apt-get clean

# Install bottle, fabric, netifaces for Python 2
RUN pip2 install bottle fabric netifaces

# Install bottle, netifaces for Python 3
RUN pip3 install bottle netifaces

# Change the adduser.conf file
COPY adduser.conf /etc/adduser.conf

# Change the login.defs file
COPY login.defs /etc/login.defs

# Change the login.html file
COPY login.html /usr/local/share/jupyter/hub/templates/login.html 

# Add logos for footer
COPY logos/ig_logo_150x50px.png /usr/local/share/jupyter/hub/static/images/ig_logo_150x50px.png
COPY logos/us_plus_intibs_logo_81x50px.png /usr/local/share/jupyter/hub/static/images//us_plus_intibs_logo_81x50px.png
COPY logos/efrr_logo_204x50px.png /usr/local/share/jupyter/hub/static/images/efrr_logo_204x50px.png

# Expose a port
EXPOSE 9797

# Add the authscript_back_end.py file
COPY scripts/authscript_back_end.py authscript_back_end.py

# Change the 'jupyterhubscript' file
COPY jupyterhubscript jupyterhubscript
