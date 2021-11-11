FROM ubuntu:20.04

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt update
RUN apt -y upgrade
RUN apt -y install curl wget dialog apt-utils libx11-6 libusb-1.0-0 libexpat1 libglu1-mesa libglib2.0-0 libfreetype6 python3 python3-dev libcec4 gnupg gnupg2 lsb-core

# RUN wget $(curl -s https://api.github.com/repos/hyperion-project/hyperion.ng/releases | python3 -c "import sys, json, urllib.request; print([i['browser_download_url'] for i in json.loads(urllib.request.urlopen(urllib.request.Request('https://api.github.com/repos/hyperion-project/hyperion.ng/releases')).read().decode('utf-8'))[0]['assets'] if 'x86_64.deb' in i['browser_download_url']][0])")
# RUN dpkg -i --force-depends ./Hyperion-*-Linux-x86_64.deb

# RUN rm Hyperion-*-Linux-x86_64.deb

RUN wget -qO- https://apt.hyperion-project.org/hyperion.pub.key | gpg --dearmor -o /usr/share/keyrings/hyperion.pub.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/hyperion.pub.gpg] https://apt.hyperion-project.org/ $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/hyperion.list
RUN apt -y update
RUN apt -y install hyperion

CMD ["hyperiond"]
