# 2020SummerResearch 
Requires anaconda and python  
**Installation of Required Materials**  
`conda env create -f config/environment.yml` if no environment exists already  
`conda env update --prefix ./env --file config/environment.yml  --prune` to update an existing environment  
`conda activate python`  
`jupyter lab workspaces import config/lab.json`  
`jupyter labextension install @jupyter-widgets/jupyterlab-manager`        
###running the program  
`jupyter lab`  
run all the code cells to get a GUI

##Using Pip
While pip will probably not work and you will regret it, here is how to use pip  
`pip install config/requirements.txt`  
`jupyter nbextension enable --py widgetsnbextension`  
`jupyter lab workspaces import config/lab.json`  
`jupyter labextension install @jupyter-widgets/jupyterlab-manager`        
###running the program
`jupyter lab`  
##Developing this further:

Export jupyter lab files  
`jupyter lab workspaces export > config/lab.json`  

