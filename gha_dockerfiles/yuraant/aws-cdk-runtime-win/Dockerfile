# escape=`

FROM mcr.microsoft.com/windows/servercore:ltsc2019
SHELL ["powershell", "-Command"]

ARG Aws_Powershell_Version=4.1.9.0
ARG PS_SqlServer_Module_Version=21.1.18245
ARG Node_Version=16.10.0
ARG Npm_Version=7.24.1
ARG Aws_Cli_Version=2.2.43
ARG Powershell_Version=7.1.3
ARG Octopus_Cli_Version=7.4.3145
ARG Octopus_Client_Version=11.1.2
ARG Aws_Cdk_Version=1.125.0

# Install Choco
RUN $ProgressPreference = 'SilentlyContinue'; `
    Set-ExecutionPolicy Bypass -Scope Process -Force; `
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
    iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install dotnet 3.1+
RUN Invoke-WebRequest 'https://dot.net/v1/dotnet-install.ps1' -outFile 'dotnet-install.ps1'; `
    [Environment]::SetEnvironmentVariable('DOTNET_CLI_TELEMETRY_OPTOUT', '1', 'Machine'); `
    .\dotnet-install.ps1 -Channel '3.1'; `
    rm dotnet-install.ps1


## Install AWS PowerShell module
## Install PowerShell SqlServer module
## https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up-windows.html#ps-installing-awspowershellnetcore
RUN Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force; `
    Install-Module -name AWSPowerShell.NetCore -RequiredVersion $Env:Aws_Powershell_Version -Force; `
    Install-Module -Name SqlServer -RequiredVersion $Env:PS_SqlServer_Module_Version -Force

## Install NodeJS
RUN choco install nodejs -y --version $Env:Node_Version --no-progress

## Update npm
RUN npm install -g npm@$Env:Npm_Version

# Install the AWS CLI
RUN choco install awscli -y --version $Env:Aws_Cli_Version --no-progress

## Install Powershell Core
RUN choco install powershell-core --yes --version $Env:Powershell_Version --no-progress

## Install octo
RUN choco install octopustools -y --version $Env:Octopus_Cli_Version --no-progress

## Install Octopus Client
RUN Install-Package Octopus.Client -source https://www.nuget.org/api/v2 -SkipDependencies -Force -RequiredVersion $Env:Octopus_Client_Version

## Install aws-cdk
RUN npm install -g aws-cdk@$Env:Aws_Cdk_Version

## Update path for new tools
ADD .\scripts\update_path.cmd C:\update_path.cmd
RUN .\update_path.cmd;
