# Perform the build in an Unreal Engine development container image that includes the Engine Tools
FROM adamrehn/ue4-full:4.21.2 AS builder

# Clone the source code for our Unreal project
RUN git clone --progress --depth 1 https://github.com/adamrehn/ue4-sample-project.git /tmp/project

# Build and package our Unreal project
# (We're using ue4cli for brevity here, but we could just as easily be calling RunUAT directly)
WORKDIR /tmp/project
RUN ue4 package

# Copy the packaged files into a runtime container image that doesn't include any Unreal Engine components
FROM adamrehn/ue4-runtime:latest
COPY --from=builder --chown=ue4:ue4 /tmp/project/dist/LinuxNoEditor /home/ue4/project