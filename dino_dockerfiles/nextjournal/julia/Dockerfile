FROM julia:0.6.0

RUN apt-get update && apt-get install -y bash curl git coreutils unzip build-essential cmake lsb-release libx11-dev libxt-dev libxft-dev libgl1-mesa-dev

RUN julia -e 'Pkg.add("DataFrames"); Pkg.add("PlotlyJS"); Pkg.add("Feather"); Pkg.add("Plots")'
RUN julia -e 'for pkg in keys(Pkg.installed()); try info("Compiling: $pkg"); eval(Expr(:toplevel, Expr(:using, Symbol(pkg)))); catch err warn("Unable to precompile: $pkg"); warn(err); end end'

RUN mkdir -p /wrappers
COPY shell.sh /wrappers/shell.sh
