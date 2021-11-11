# Use official Python 2 release
FROM python:2

# Maintainer
LABEL maintainer="Björn Gernert <mail@bjoern-gernert.de>"

# Update Ubuntu image
RUN apt-get -qq update && apt-get -qq upgrade

# Install Munin
RUN apt-get -qq install --no-install-recommends unzip

# Clean up updates/install
RUN apt-get -qq autoclean && apt-get -qq autoremove && apt-get -qq clean

# Install dependencies
RUN pip install --upgrade google-api-python-client progressbar2

# Install youtube-upload
RUN cd /root && wget https://github.com/tokland/youtube-upload/archive/master.zip && unzip master.zip && cd youtube-upload-master && python setup.py install

# Clean up
RUN rm -r /root/master.zip /root/youtube-upload-master

# Create credentials file
RUN touch /root/.youtube-upload-credentials.json

# Add help message to .bashrc
RUN echo "\
\n\
echo How to use:\n\
echo - Videos are mounted in /videos\n\
echo - Run \'youtube-upload --title=\'My Video\' --privacy unlisted /videos/my_video.avi\' to upload videos\n\
echo - For more information type \'youtube-upload --help\'\n\
echo \n\
" >> /root/.bashrc

# Export volumes
VOLUME /videos

# Start bash
CMD ["/bin/bash"]
