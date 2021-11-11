FROM ubuntu
MAINTAINER Marchand D. https://github.com/marchandd/term_ssh_user_monodotnet45
ENV VE_version="MarchandD_20151117_v02.01" 
RUN apt-get update && apt-get install -y openssh-server firefox supervisor dbus-x11 pwgen
RUN mkdir /var/run/sshd
# Copy user script from local to root and run it
COPY ./usercreation.sh /
RUN chmod 755 /*.sh
RUN bash -c '/usercreation.sh'
#Mono from Xamarin
RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | sudo tee /etc/apt/sources.list.d/mono-xamarin.list
RUN apt-get update -y && apt-get install -y mono-complete
# Supervisor settings for ssl
COPY ./supervisor/supervisor.conf /etc/supervisor/supervisor.conf
RUN chmod 775 /etc/supervisor/*.conf
COPY ./supervisor/ssl.conf /etc/supervisor/conf.d/
RUN chmod 775 /etc/supervisor/conf.d/ssl.conf
# SSL port
EXPOSE 22
# Directory ready
WORKDIR /etc/supervisor
# Supervisor daemon
CMD supervisord -c /etc/supervisor/supervisor.conf
