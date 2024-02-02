# Ensuring environment stability in online reinforcement learning via critic as Lyapunov function

This repository contains the code for reproducing the experiments described in the paper "Ensuring environment stability in online reinforcement learning via critic as Lyapunov function".

Experiments can be reproduced by running simulations with various agents and environments (systems). Two options are available for running these experiments:

1. [**From the Source:**](#running-experiments-from-source-on-linux) This method involves setting up a Python virtual environment, installing dependencies, and executing the experiments manually.
2. [**Using Docker:**](#running-experiments-using-docker) This method uses Docker to handle dependencies and environment setup automatically, allowing for easy reproduction of experiments. For detailed instructions and guidance on installing Docker, we encourage the reader to consult the official [Docker documentation](https://docs.docker.com/engine/install/). 

The minimal system requirements for optimal performance are specified below:

- RAM: 32GB or higher
- CPU Cores: At least 16 logical cores
- Storage space: 250 GB for all experiment data

## Table of contents

* [Running Experiments From Source (on Linux)](#running-experiments-from-source-on-linux)
  * [Setup Python Virtual Environment](#setup-python-virtual-environment)
  * [Running the Experiments](#running-the-experiments)
* [Running Experiments Using Docker](#running-experiments-using-docker)
* [Viewing Experiment Results](#viewing-experiment-results)
  * [From Source](#from-source)
  * [Using Docker](#using-docker)
* [Abbreviations](#abbreviations)
  * [Systems (Environments)](#systems-environments)
  * [Agents](#agents)

## Running Experiments From Source (on Linux)

### Setup Python Virtual Environment

Note that this project requires **Python version 3.9 or newer, but not beyond 3.11**.

Before running the experiments from the source, it is recommended to setup a virtual environment to isolate the project dependencies. Here's how to do it:

1. **Install virtualenv if you haven't got it installed:**

   ```bash
   pip install virtualenv
   ```
   
2. **Create a virtual environment:**

   Navigate to the root of the repo and run:

   ```bash
   virtualenv venv
   ```
   
3. **Activate the virtual environment:**


   ```bash
   source venv/bin/activate
   ```
  
### Running the Experiments

Once the virtual environment is activated, run the experiments using the following steps:

1. Install the package:

   ```bash
   sudo apt update
   sudo apt install -y libgeos-dev libqt5x11extras5 default-jre
   pip install ./rehydra
   pip install ./rehydra/plugins/rehydra_joblib_launcher
   pip install -e .
   ```

2. Change to the `presets` directory:

   ```bash
   cd presets
   ```
   
3. Run the `reproduce.py` script with the necessary parameters:

   ```bash
   python reproduce.py --agent={NAME_OF_THE_AGENT} --system={NAME_OF_THE_SYSTEM}
   ```
  
   Replace `{NAME_OF_THE_AGENT}` and `{NAME_OF_THE_SYSTEM}` with the corresponding short names from the lists [below](#abbreviations). For instance,
   ```bash
   python reproduce.py --agent=ppo --system=inv_pendulum
   ```



## Running Experiments Using Docker

For those who prefer Docker, the setup is simplified. Just run in the root of the repo:

```bash
sudo docker compose run reproduce.py --agent=ppo --system=inv_pendulum
```

Replace `ppo` and `inv_pendulum` with the desired [agent and system abbreviations](#abbreviations), respectively. We warn you that the command downloads a large (6GB) image, which may take 10-15 minutes to complete.

## Viewing Experiment Results

### From Source

For experiments run from the source code:

1. Navigate to the `srccode_data` folder inside the `presets` directory. This folder is created after running the `reproduce.py` script.
2. Start the [MLflow](https://mlflow.org/) tracking server:

   ```bash
   mlflow ui --port=5000 --host=0.0.0.0
   ```
3. Access the experiment results by visiting http://localhost:5000

### Using Docker

[MLflow](https://mlflow.org/) is configured to start automatically during the execution of the run command 
```bash
sudo docker compose run reproduce.py --agent={NAME_OF_THE_AGENT} --system={NAME_OF_THE_SYSTEM}
```
so there's no need for manual initiation. Once the experiments have concluded, open your preferred web browser and visit http://localhost:5000 to view the results. 

To stop the MLflow tracking server just write in the root of the repo
```bash
sudo docker compose stop
```


## Abbreviations

### Systems (Environments)

- `--system=cartpole` for the cartpole
- `--system=inv_pendulum` for the inverted pendulum
- `--system=3wrobot_kin` for the three-wheel robot
- `--system=2tank` for the two-tank system
- `--system=lunar_lander` for the lunar lander
- `--system=kin_point` for the omnibot (kinematic point)

### Agents

- `--agent=calf` for Critic as Lyapunov Function (**ours**)
- `--agent=nominal` for $\pi_0$ 
- `--agent=ppo` for Proximal Policy Optimization (PPO)
- `--agent=sdpg` for Vanilla Policy Gradient (VPG)
- `--agent=ddpg` for Deep Deterministic Policy Gradient (DDPG)
- `--agent=reinforce` for REINFORCE
