FROM jupyter/r-notebook:7fd175ec22c7

MAINTAINER Daniel Davis <dan@danizen.net>

USER root

# Don't delete this user as it is embedded in the pip configuration, even for root
# 
# RUN userdel jovyan && rm -rf /home/jovyan

COPY requirements.txt /srv/singleuser/requirements.txt

# Install additional python packages
RUN pip install -r /srv/singleuser/requirements.txt

# Enable jupyter extensions
RUN jupyter contrib nbextensions install
RUN jupyter nbexension enable help_panel/help_panel
RUN jupyter nbexension enable varInspector/main

# Install notebooks into the user skeleton directory
COPY notebooks/ /etc/skel/

# Switch back to user jovyan and whatever is the default command-there
USER jovyan

# Copy the notebooks again
COPY notebooks/ /home/jovyan/

# Remove the distracting work directory
RUN rm -rf /home/jovyan/work/

