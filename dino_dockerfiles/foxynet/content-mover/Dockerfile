FROM photon:1.0

# Set Versions for later use
ARG POWERCLI_PACKAGE=PowerCLI.ViCore.zip
ARG POWERCLI_VDS_PACKAGE=PowerCLI.Vds.zip

# Add PowerShell repository location to Photon OS
RUN echo $'[powershell]\n\

name=VMware Photon Linux 1.0(x86_64)\n\
baseurl=https://vmware.bintray.com/powershell\n\
gpgcheck=0\n\
enabled=1\n\
skip_if_unavailable=True\n '\
>> /etc/yum.repos.d/powershell.repo

# Set the working directory 
WORKDIR /powershell

# Install PowerShell on Photon 
RUN tdnf install -y unzip powershell curl openssl

# Download and Unzip the PowerCLI module to the users module directory
ADD https://download3.vmware.com/software/vmw-tools/powerclicore/PowerCLI_Core.zip /powershell
RUN unzip /powershell/PowerCLI_Core.zip -d /powershell
RUN mkdir -p /root/.config/powershell/
RUN mkdir -p ~/.local/share/powershell/Modules
RUN unzip /powershell/$POWERCLI_PACKAGE -d ~/.local/share/powershell/Modules
RUN unzip /powershell/$POWERCLI_VDS_PACKAGE -d ~/.local/share/powershell/Modules

# Change the default PowerShell profile to include PowerCLI startup
RUN mv /powershell/Start-PowerCLI.ps1 /root/.config/powershell/Microsoft.PowerShell_profile.ps1

# Install ovftool
ENV OVFTOOL_VERSION 4.2.0-4586971

ENV OVFTOOL_INSTALLER=VMware-ovftool-${OVFTOOL_VERSION}-lin.x86_64.bundle

RUN tdnf install -y ncurses-compat gawk tar sed gzip

ADD https://s3-us-west-2.amazonaws.com/knacker/${OVFTOOL_INSTALLER} /usr/local

RUN chmod +x /usr/local/${OVFTOOL_INSTALLER}
RUN mkdir -p /etc/init.d/

RUN /usr/local/${OVFTOOL_INSTALLER} -p /usr/local --eulas-agreed --required

RUN rmdir /etc/init.d

CMD ["powershell"]
