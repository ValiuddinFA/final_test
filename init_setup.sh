echo [$(date)]: "START"
echo [$(date)]: "Creating Conda Env with Python 3.10" #change py version as per requirement
conda create --prefix ./env python=3.10 -y
echo [$(date)]: "Activating env"
source activate env
echo [$(date)]: "Installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"