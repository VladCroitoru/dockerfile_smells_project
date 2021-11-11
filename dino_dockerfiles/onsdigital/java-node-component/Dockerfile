FROM onsdigital/java-component

# Node.js

# The tar and bzip2 packages are required for Phantom.js installation in npm: https://github.com/Medium/phantomjs/issues/326
RUN apt-get install -y curl tar bzip2

# We need to use a later version of Node than is currently available in the Ubuntu package manager (2015-06-17)
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get install -y nodejs
