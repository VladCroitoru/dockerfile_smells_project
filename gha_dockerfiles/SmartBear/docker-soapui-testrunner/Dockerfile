FROM smartbear/ready-api-soapui-testrunner:latest

RUN apt-get update -y && apt-get upgrade -y

##### USE CASE 1: add a ReadyAPI project to a Docker image

# You need to provide a container with a project file and all the dependent files.
# You can specify these files in the command line you use to run the container.
# It is possible to add the files to a Docker image. In this case, you can omit the 
# -v="Project folder":/project option in the command line. Note that you will
# still have to specify the project name in the COMMAND_LINE variable.
# Note that files you want to add must be in the build context.
# To include the files in a Docker image, use the following lines:

# RUN mkdir -p $PROJECT_FOLDER
# ADD projects/sample-readyapi-project $PROJECT_FOLDER

##### USE CASE 2: specify the license server address in a Docker image

# To run SoapUI tests in a container, you need a SoapUI floating license.
# You can specify the address of the license server when you run the container by using
# the -e LICENSE_SERVER="License server address" option, or you can specify this
# information in a Docker image:

# ENV LICENSE_SERVER=10.0.10.1:1099

##### USE CASE 3: add external libraries to ReadyAPI's bin/ext folder

# If you use external libraries in your test, you must put them to ReadyAPI's 
# bin/ext folder. For example, if you interact with a database, you will have 
# to put a JDBC driver there. It is possible to add this file to a Docker image.
# In this case, you can omit the -v="Extensions Folder":/ext option in the command line.
# Note that the libraries you want to add must be in the build context.
# To add the libraries to a Docker image, use the following line:

# ADD readyapi/ext $READYAPI_FOLDER/bin/ext

##### USE CASE 4: add plugins to a Docker image

# If you use plugins in your test, you must install them to ReadyAPI in a container. 
# For example, if you run your test by using the MQTT or AMQP protocols, you must install 
# the related plugins. It is possible to add them to a Docker image. In this case,
# you can omit `-v="Plugins folder":/root/.soapui/plugins` in the command line. 
# Note that the plugin files you want to add must be in the build context.
# To add plugins to a Docker image, use the following line:

# ADD plugins /root/.soapui/plugins

##### USE CASE 5: specify a command line in a Docker image

# When you run a container, it runs the SoapUI test runner via the command line 
# specified in the COMMAND_LINE environment variable. You can add this
# command line to a Docker image. In this case, you will be able to skip the 
# -e COMMAND_LINE="Test runner arguments". To add the command line,
# use the following line:

# ENV COMMAND_LINE="-f/%reports% '-RJUnit-Style HTML Report' -FHTML '-EDefault environment' '/%project%/sample-readyapi-project.xml'"