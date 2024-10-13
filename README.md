# Advanced Persistent Threats Attribution usnign Deep Reinforcement Learning - ACM DTRAP

## Abstract

Advanced Persistent Threats (APTs) are a class of cyber-attacks that are characterized by their stealthy and persistent nature. APTs are often state-sponsored and are designed to remain undetected for long periods of time. The ability to attribute APTs to their respective threat actors is crucial for understanding the motives and capabilities of the attackers. However, APTs are designed to be stealthy and attribution is a challenging task. In this paper, we propose a novel approach for APT attribution using deep reinforcement learning (DRL). We model the APT attribution problem as a Markov Decision Process (MDP) and use DRL to learn the optimal policy for attributing APTs to their respective threat actors. We evaluate our approach using a dataset of APTs and show that our approach outperforms existing methods for APT attribution.

##  Dataset

The dataset used in this paper is a collection of APTs obtained from https://github.com/cyber-research/APTMalware. This dataset contains over 3,500 malware samples that are related to 12 APT groups which alledgedly are sponsored by 5 different nation-states. 

## Files

The scripts for the code is broken down into the following files:

1. `Cuckoo_task_id_extractor.ipynb`- This notebook contains the code for extracting the Cuckoo task ids from the dataset.
2. `Cuckoo_auto_download_script.py` - This script contains the code for downloading the Cuckoo reports for the malware samples.
3. `Cuckoo_feature_extraction.ipynb` - This notebook contains the code for extracting the features from the Cuckoo reports.
4. `VirusTotal_extract_reports.ipynb` - This notebook contains the code for extracting the VirusTotal reports for the malware samples.
5. `Apt_attribution_using_drl.ipynb` - This is the main notebook that contains the code for training and evaluating the DRL model for APT attribution.
