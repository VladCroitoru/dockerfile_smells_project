FROM lapidarioz/docker-cpp-opencv3-glut

# https://stackoverflow.com/questions/16296753/can-you-run-gui-apps-in-a-docker-container
RUN apt-get update && apt-get install -y x11vnc xvfb
# RUN yes 1 | apt-get install -y xorg
RUN apt-get install -y openbox

RUN mkdir /.vnc
# Setup a password
RUN x11vnc -storepasswd 1234 /.vnc/passwd

# Build the RK (Runge-Kutta) suite
WORKDIR /
RUN wget http://www.netlib.org/ode/rksuite/rksuitec++.zip && unzip rksuitec++.zip
WORKDIR /RksuiteTest
RUN gcc -c -fPIC rksuite.cpp -o rksuite.o -w
RUN gcc -shared -o librksuite.so rksuite.o
RUN cp librksuite.so /usr/lib/
RUN cp rksuite.h /usr/include

ENV HOME /

COPY . /usr/src/box
WORKDIR /usr/src/box
RUN gcc -o box box.cpp -DUNIX -O2 -w -Wall -s -lglut -lGLU -lGL -L/usr/X11R6/lib -lXi -lXmu -lX11 -lm -lrksuite -lstdc++ 

CMD ./entrypoint.sh
