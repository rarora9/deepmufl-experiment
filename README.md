# deepmufl-experiment

- The source code for deepmufl is included in the folder deepmufl-ase-2023-main/src/. This code is based on the deepmufl code by Ghanbari et al. with some modifications, which is available at https://github.com/ali-ghanbari/deepmufl-ase-2023.
- model_test_data.ipynb was used to create the trained models, inputs, and ouputs.
- The trained models, inputs, and outputs that are used as input to deepmufl are in the folder deepmufl-ase-2023-main/models. Each model has 3 replicas (folders "01", "02", "03). Within the replica folders are the trained models, inputs and outputs. In addition, there are 4 files (25.txt, 50.txt, 75.txt, 100.txt) which are the output files for 25%, 50%, 75%, and 100% mutation selection.
- create_deepmufl_command.py was used to create the command which runs all of the models with deepmufl. This was done to avoid having to manually enter 144 commands in total.
- All of the 25.txt, 50.txt, 75.txt, 100.txt files are analyzed by generate_metrics.ipynb to obtain fault localization results. The results are in experiment_results.xlsx.
- original_deepmufl_results.xlsx contains results from the original paper by Ghanbari et al., but only including the models that were used in this experiment. These results can be directly compared to the results in experiment_results.xlsx.
