
#Intall desire docker container
FROM node  

#Create a working directory into docker container
WORKDIR /app

#Copy Package.json file to working dir into docker container (whenever, this dockerfile runs, firs it will check, is there any changes into this file, if yes then and then only it will run "npm install command", by doing this build command will take lesser time (kind of "image layer OR image optimization") )
COPY package.json /app

#Intall packages from package.json depencies 
RUN npm install

#Copy current project to app dir into docker container 
COPY . /app


#This is optional but good for best practice (real one is when we run "docker run -p :xx:xx")
EXPOSE 80

#Now, run node main file whatever declared as "main" key into package.json file (here for eg. 'server.js')
CMD ["node", "server.js"]