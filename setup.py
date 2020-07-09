import os

def install(Jupyter = True):
    if (os.environ['CONDA_DEFAULT_ENV'] != "python"):
        print("Activating environment")
        os.system('conda activate python')
        if(os.environ['CONDA_DEFAULT_ENV'] != "python"):
            print("Failed: Environment doesn't exist")
            print("Creating environment: this will take a while")
            os.system('conda env create -f config/environment.yml')
            os.system('conda activate python')
        else:
            print("environment exists")
            os.system('conda env update --name python --file config/environment.yml')
    else:
        print("Updating environment")
        os.system('conda env update --name python --file config/environment.yml')
    if(Jupyter):
        print("Configuring Jupyter:")
        os.system('jupyter lab workspaces import config/lab.json')
        os.system('jupyter labextension install @pyviz/jupyterlab_pyviz')
        os.system('jupyter labextension install @jupyter-widgets/jupyterlab-manager')
def run():
    os.system('panel serve holoviz.ipynb')
install()
run()
