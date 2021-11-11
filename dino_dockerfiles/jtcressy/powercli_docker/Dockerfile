FROM vmware/powerclicore
#Allow connections to servers with non-verified CA certificates
RUN powershell Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:\$false
