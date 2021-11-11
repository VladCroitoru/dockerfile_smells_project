############################################################
# Dockerfile to build HN-sum server                        #
# Based on Ubuntu                                          #
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER Nicholas Rutherford

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential


###########################################
#         Setup python script             #
###########################################
# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute

# Get pip
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

# Get application
RUN git clone https://github.com/nicholasRutherford/HN-sum.git

# Get pip to download and install requirements:
RUN pip install -r /HN-sum/requirements.txt

# Download NLTK data:
RUN python /HN-sum/bin/nltkSetup.py

# Set up the inital website
RUN cd /HN-sum/ && python hnSummarized/updateWebsite.py

# Set update to run hourly
RUN cp /HN-sum/bin/updateWeb.sh /etc/cron.hourly/updateWeb


###########################################
#            Set up Nginx                 #
###########################################
# Download and Install Nginx
RUN apt-get install -y nginx


# Copy a configuration file from the current directory
ADD deploy/hn-sum.info /etc/nginx/sites-available/hn-sum.info

# Link
RUN ln -s /etc/nginx/sites-available/hn-sum.info /etc/nginx/sites-enabled/

# Remove default
RUN rm /etc/nginx/sites-enabled/default

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

# Set the default directory where CMD will execute
WORKDIR /HN-sum

# Set the default command to execute
# when creating a new container
CMD cron && service nginx start
