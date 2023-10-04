
# tut
[Data Cleaning and Exploratory Data Analysis with Pandas on Trending Youtube Video Statistics](https://medium.com/@raahimkhan_85173/data-cleaning-and-exploratory-data-analysis-with-pandas-on-trending-you-tube-video-statistics-e06d7cd08710)

# dataset
https://www.kaggle.com/datasnaek/youtube-new

# 'conda' data science env

## install
https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

## getting started
[conda : getting started](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
```
conda --version

conda update conda

conda create --name data-cleaning-0 pandas jupyter seaborn matplotlib

conda activate data-cleaning-0

# list all envs
conda info --envs

# packages
conda list  # list installed packages
conda install beautifulsoup4  # install a package
conda search beautifulsoup4  # search for package

```

# jupyter
[getting started with jupyter](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
```
# install
conda install jupyter
conda install pandas matplotlib

# create new
jupyter notebook data-cleaning-0.ipynb

```

# troubleshooting
## character encodings
https://www.kaggle.com/code/alexisbcook/character-encodings

# google cloud
[running-jupyter-notebook-in-google-cloud](https://towardsdatascience.com/running-jupyter-notebook-in-google-cloud-platform-in-15-min-61e16da34d52)

# project
heidless-jupyter-0

# config VM instance

Compute Engine:
jupyter-instance-0
35.246.15.138

SSH:
wget http://repo.continuum.io/archive/Anaconda3-5.3.1-Linux-x86_64.sh

bash Anaconda3-5.3.1-Linux-x86_64.sh

sudo apt update
sudo apt upgrade

python -m pip install --upgrade pip
pip3 install opencv-python


STATIC_IP: 
heidless-static-ip
35.214.40.106

FIREWALL:
heidless-firewall-0

PORT: 5000

# ssh console of compute engine instance
jupyter-notebook --no-browser --port=5000

# access instance
http://35.214.40.106:5000?token=edcda05bea66e338f81aa039cb1c4650379b37a04760ac3d

# Vertex AI: jupyterlabs
[vertex AI](https://console.cloud.google.com/vertex-ai/workbench/managed?_ga=2.221845912.1259457075.1695372669-781479075.1695370673&_gac=1.16709316.1695370673.Cj0KCQjw9rSoBhCiARIsAFOiplmOq1mogbbRUAkHL_5PWvfAiD4_ma8ieKVbx0fhcLeX_Ye5ftOqoNMaAsWUEALw_wcB&project=heidless-jupyter-0)

## init notebook
[google cloud manage notebooks](https://console.cloud.google.com/vertex-ai/workbench/managed?_ga=2.221845912.1259457075.1695372669-781479075.1695370673&_gac=1.16709316.1695370673.Cj0KCQjw9rSoBhCiARIsAFOiplmOq1mogbbRUAkHL_5PWvfAiD4_ma8ieKVbx0fhcLeX_Ye5ftOqoNMaAsWUEALw_wcB&project=heidless-jupyter-0)

## connect to cloud storage
[google cloud storage access](https://cloud.google.com/vertex-ai/docs/workbench/managed/cloud-storage)

## initialise data
### Copy from your bucket to local path (note -r is for recursive call)
```
!gsutil cp -r gs://heidless-jupyter-bucket-0/jupyter-data/clean-0 /home/heidlessemail0/data/clean-0
```
!gsutil cp -r gs://BUCKET/DIR_PATH ./TARGET_DIR

heidless-jupyter-bucket-0/jupyter-data/clean-0

# data cleaning notes
- import data
- rationalise data types & values
- misssing values
