# Pcap filter with GPT

## How it works?
![Alt Text](./demo.gif)

## Installation
You need to have Conda and a MySQL server installed in your machine. Steps for installing and configuring MySQL server on Ubuntu 20.04 are available in `install.sh`. However, if you have a different Operating System, you will need to install them before running the script. 

`install.sh` contains code for creating the conda environment and installed the required python packages. After executing the script and creating the required environment, you will need to set up some local variables explained next:

### Setting up your OPEN_API_KEY
You will need to create a `.env` file at the root of the project. After that, write the following line in it:

```env
OPENAI_API_KEY="YOUR KEY"
```
The `.env` file will not be pushed to Github, therefore your API key will not be shown in the repository.

### Setting up your MySQL username and password
Inside the same `.env` file created before, add the following:
```env
MYSQL_USER="XXX"
MYSQL_PASSWORD="XXX"
```
The `.env` file will not be pushed to Github, therefore your user and password will not be shown in the repository.

## Run Command Line Tool
An running example can be seen at the gif file in section [How it works?](#how-it-works). Next are the commands that need to be run.

```shell
conda activate pcap_gpt
python cli.py -pcap {$PCAP_FILE} - q "{$QUERY}"
```

## Run Experiment
To evaluate our tool, we designed 4 experiments. A summary of them are showed in the next table.

| Exp # |      Evaluation     |
|:-----:|:-------------------:|
|   1   |   Original Queries  |
|   2   |  English Variations |
|   3   | Language Variations |
|   4   | Adversarial Attacks |

To execute an experiment, run the following commands in your terminal:

```shell
conda activate pcap_gpt
python experiment.py {[-exp1, -exp2, -exp3, -exp4]}
```