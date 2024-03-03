def create_deepmufl_command():
  model_num = "01"

  model_dirs = [
      "33969059_reg_final_layer_softmax",
      "34311586_reg_final_layer_softmax",
      "48221692_reg_final_layer_sigmoid",
      "48486598_reg_hidden_layer_linear",
      "56774954_reg_final_layer_softmax",
      "59758722_reg_final_layer_relu",
      "31880720_class_final_layer_softmax",
      "41823068_class_final_layer_sigmoid",
      "41999686_class_final_layer_sigmoid",
      "42472447_class_final_layer_sigmoid",
      "51185079_class_final_layer_relu",
      "58844149_class_final_layer_softmax",
  ]
  mutation_selection_rates = ["1.0", "0.75", "0.5", "0.25"]

  command = ""

  for model_dir in model_dirs:
    model_id = model_dir[0:8]
    model_type = "reg"
    if model_dir[9:12] != "reg":
      model_type = "class"
    if command:
      command = f"{command} &&"
    command = f"{command} cd ../../{model_dir}/{model_num}/"
    for mutation_selection_rate in mutation_selection_rates:
      command = f"{command} && python ../../../src/main.py {model_num}_{model_id}.h5 {mutation_selection_rate} {model_num}_{model_id}_X_test.npy {model_num}_{model_id}_y_test.npy {model_type} 0.001"
    command = f"{command} && rm workdir.tar.gz"

  print(command)
