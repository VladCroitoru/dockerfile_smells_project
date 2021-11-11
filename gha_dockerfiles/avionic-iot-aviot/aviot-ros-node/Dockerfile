FROM ros:kinetic

RUN apt-get update
RUN apt-get install -y wget curl git

# Install Node
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y ros-kinetic-mavros ros-kinetic-mavros-extras

# Building geofence messages
RUN mkdir -p /root/catkin_ws
COPY devel /root/catkin_ws/devel
#RUN . /root/catkin_ws/devel/setup.sh

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

# Bundle app source
COPY . .

RUN git submodule init
RUN git submodule update

WORKDIR /usr/src/app/src/services/rosnodejs
RUN npm install
RUN npm run compile

WORKDIR /usr/src/app
RUN npm install

# If you are building your code for production
# RUN npm ci --only=production

EXPOSE 8080
CMD [ "npm", "run", "prod" ]

