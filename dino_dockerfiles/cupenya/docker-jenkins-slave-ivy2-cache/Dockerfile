# The MIT License
#
#  Copyright (c) 2015, CloudBees, Inc.
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.

FROM cupenya/docker-jenkins-slave-services
MAINTAINER Elmar Weber <elmar(.)weber(@)cupenya(.)com>

# add ivy2 cache
USER root

# should be this, but it adds two layers of a few hundred MB just for the
# chown due to Dockers approach, therefore the download is done inside the
# image to keep it smaller
# COPY ivy2-cache /home/jenkins/.ivy2/cache
# RUN chown jenkins:jenkins -R /home/jenkins/.ivy2

#RUN mkdir /tmp/ivy2-init && \
#    cd /tmp/ivy2-init && \
#    wget https://github.com/cupenya/docker-jenkins-slave-ivy2-cache/archive/master.zip && \
#    unzip master.zip && \ 
#    mkdir /home/jenkins/.ivy2 && \
#    cp -r docker-jenkins-slave-ivy2-cache-master/ivy2-cache /home/jenkins/.ivy2/cache && \
#    chown jenkins:jenkins -R /home/jenkins/.ivy2 && \
#    cd /tmp && \
#    rm -Rf ivy2-init

# reset to parent user
USER jenkins
