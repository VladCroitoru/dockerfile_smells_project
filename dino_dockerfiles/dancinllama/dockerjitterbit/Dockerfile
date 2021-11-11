# This image provides an environment with the Jitterbit Agent (v 8.17) installed.
# To run the docker image, enable port forwarding of the default agent port 46908.
# (E.g.: docker run -itp 46908:46909 dancinllama/jitterbit
# After the image runs, you will need to:
#     1) Configure it.  
#     2) Run it.  
#     3) Log into your harmony account and make sure it is running.
# To configure it, run /opt/jitterbit/bin/jitterbit-config
# When configuring, you'll need your harmony username and password.
# More instructions can be found here: 
#     https://success.jitterbit.com/display/DOC/Download+and+Install+Harmony+Linux+Agent
FROM library/ubuntu
RUN dpkg --add-architecture i386 && \
	apt-get update && \
	apt-get -y install libc6:i386 libgcc1:i386 \
		libstdc++6:i386 libuuid1:i386 \
		zlib1g:i386 unixodbc python \
		sed sudo unzip tar && \
	apt-get -y install wget && \
        wget https://download.jitterbit.com/v8/agent/8.17/jitterbit-agent_8.17.0.2_i386.deb && \
	dpkg --install jitterbit*.deb
