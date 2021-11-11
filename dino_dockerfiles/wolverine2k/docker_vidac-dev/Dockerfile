# Build: docker build -f node.vidac.dockerfile -t wolverine2k/node_vidac .

# Option 1
# Start MongoDB and Node (link Node to MongoDB container with legacy linking)
 
# docker run -d --name my-mongodb mongo
# docker run -d -p 3000:3000 -p3001:3001 --link my-mongodb:mongodb --name vis wolverine2k/node_vidac
# Option 2: Create a custom bridge network and add containers into it

# docker network create --driver bridge isolated_network
# docker run -d --net=isolated_network --name mongodb mongo
# docker run -d --net=isolated_network --name vis -p 3000:3000 -p 3001:3001 wolverine2k/node_vidac

# Run the VIS application with the proper config file
# Run: docker exec vis node src/app/vis/vis_
# Run: docker exec ems node src/app/ems/ems_

#FROM node:6.3.1
FROM node:5.12.0

MAINTAINER Naresh Mehta

# Install build-essentials
USER root
RUN apt-get update && apt-get install -y build-essential

ENV NODE_ENV=development 
ENV PORT_VIS=3000
ENV PORT_EMS=3001

WORKDIR   /var/vidac

EXPOSE $PORT_VIS $PORT_EMS 27017 27018 4370 5672 5673 25673

CMD [ "/bin/bash" ]
