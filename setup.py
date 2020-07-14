import os
import argparse


def install(Jupyter=True):
    if (os.environ['CONDA_DEFAULT_ENV'] != "python"):
        print("Activating environment")
        os.system('conda activate python')
        if (os.environ['CONDA_DEFAULT_ENV'] != "python"):
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
    if (Jupyter):
        print("Configuring Jupyter:")
        os.system('jupyter lab workspaces import config/lab.json')
        os.system('jupyter labextension install @pyviz/jupyterlab_pyviz')
        os.system('jupyter labextension install @jupyter-widgets/jupyterlab-manager')


def run_bokeh(ip='',port=5006):
    os.system('panel serve holoviz.ipynb')
def run_jupyter():
    os.system('jupyter lab')
def update():
    os.system('conda env update --name python --file config/environment.yml')

parser = argparse.ArgumentParser(prog='setup',description='Install and Run python. Only one arguments execute in the following order')
parser.add_argument('--R', dest='R', help='Builds and Runs Bokeh Server (Doesn\'t install Jupyter components)',action='store_const',const=True, default= False)
parser.add_argument('--J', dest='J', help='Builds and runs Jupter Server',action='store_const',const=True, default= False)
parser.add_argument('--B', dest='B', help='Installs or Upgrades environment w/ Jupyter components',action='store_const',const=True, default= False)
parser.add_argument('--U', dest='U', help='Updates environment(NOT RECCOMENDED)',action='store_const',const=True, default= False)
args = parser.parse_args()
if args.R:
    install(False)
    run_bokeh()
elif args.J:
    install()
    run_jupyter()
elif args.B:
    install()
elif args.U:
    update()
else:
    print("No arguments given, defaulting to launching panel server")
    install()
    run_bokeh()
