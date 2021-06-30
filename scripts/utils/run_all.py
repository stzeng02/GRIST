import os
import sys

root_path = "/data/scripts/study_case/"
# root_path = "../study_case/"
file_names = [
    [""],
    ["ID_1/ghips1_grist.py"],
    ["ID_2/command_line/run_logistic_regression_grist.py",
     "ID_2/command_line/run_logistic_regression_log2_grist.py"],
    ["ID_3/ghips9_grist.py"],
    ["ID_4/test/nn/models/test_autoencoder_grist.py"],
    ["ID_5/tests/test_losses_grist.py"],
    ["ID_6/soips1_grist.py"],
    ["ID_7/soips2_grist.py"],
    ["ID_8/soips6_grist.py"],
    ["ID_9/soips7_grist.py",
     "ID_9/soips7_log2_grist.py"],
    ["ID_10/soips14_grist.py"],
    ["ID_11/nan_model_exp_grist.py",
     "ID_11/nan_model_log_grist.py",
     "ID_11/nan_model_truediv_grist.py"],
    ["ID_12/main_grist.py"],
    ["ID_13/test/utils/test_softmax_grist.py"],
    ["ID_14/v3/train_grist.py"],
    ["ID_15/train_grist.py"],
    ["ID_16/nan_model_grist.py",
     "ID_16/nan_model_log_grist.py",
     "ID_16/nan_model_truediv_grist.py"],
    ["ID_17/test_toy_grist.py"],
    ["ID_18/code_10_image_grist.py"],
    ["ID_19/mnist_grist.py"],
    ["ID_20/logistic_regression_grist.py"],
    ["ID_21/mnist_softmax_grist.py"],
    ["ID_22/My_pytorch1_grist.py"],
    ["ID_23/ch5.3_softmax_grist.py"],
    ["ID_24/Mnist_grist.py"],
    ["ID_25/mnist_grist.py"],
    ["ID_26/0401_logistic_regression_grist.py"],
    ["ID_27/0503_softmax_regression_cost_grist.py"],
    ["ID_28/sc_train_creg_grist.py",
     "ID_28/sc_train_creg_div2_grist.py",
     "ID_28/sc_train_l2reg_grist.py",
     "ID_28/sc_train_l2reg_div2_grist.py"],
    ["ID_29/temp_grist.py"],
    ["ID_30/softmax_grist.py"],
    ["ID_31/GAN_MNIST_grist.py"],
    ["ID_32/0504_softmax_regression_grist.py"],
    ["ID_33/logistic_classification_grist.py"],
    ["ID_34/softmax_classification_grist.py"],
    ["ID_35/ch10_04_01_grist.py",
     "ID_35/ch10_04_01_sqrt_grist.py"],
    ["ID_36/ch10_04_03_Pic_10_05_grist.py",
     "ID_36/ch10_04_03_Pic_10_05_sqrt_grist.py"],
    ["ID_37/lab-05-1-logistic_regression_grist.py"],
    ["ID_38/lab-09-1-xor_grist.py"],
    ["ID_39/ch10_04_04_Pic_10_06_grist.py",
     "ID_39/ch10_04_04_Pic_10_06_sqrt_grist.py"],
    ["ID_40/src/ch5/bmi_grist.py"],
    ["ID_41/src/ch5/tb-bmi_grist.py"],
    ["ID_42/src/ch5/tb-bmi2_grist.py"],
    ["ID_43/ch10_04_05_Pic_10_07_grist.py",
     "ID_43/ch10_04_05_Pic_10_07_sqrt_grist.py"],
    ["ID_44/CNN_grist.py"],
    ["ID_45/MNIST_Digit_classification_using_CNN_grist.py",
     "ID_45/MNIST_Digit_classification_using_CNN2_grist.py"],
    ["ID_46/torch20_softmax_grist.py"],
    ["ID_47/torch21_Softmax_Reg1_grist.py"],
    ["ID_48/day01_grist.py",
     "ID_48/day01_2_grist.py"],
    ["ID_49/ch10_04_06_Pic_10_08_grist.py",
     "ID_49/ch10_04_06_Pic_10_08_sqrt_grist.py"],
    ["ID_50/DL_1L_grist.py"],
    ["ID_51/rbm_grist.py"],
    ["ID_52/5_mnist_full_connection_grist.py"],
    ["ID_53/h02_20191644_grist.py"],
    ["ID_54/h03_20191644_grist.py"],
    ["ID_55/logistic_regression_grist.py"],
    ["ID_56/01_Logistic_Regression_grist.py"],
    ["ID_57/03_softmax_cost_grist.py"],
    ["ID_58/test_grist.py"],
    ["ID_59/code_06_grist.py"],
    ["ID_60/simple_saveAndReloadModel_grist.py"],
    ["ID_61/multi_layer_perceptron_grist.py"],
    ["ID_62/denoising_RBM_grist.py"],
    ["ID_63/main_grist.py"],
]

for case_idx in range(1, 64):
    for file_name in file_names[case_idx]:
        file_dir = root_path + file_name[:file_name.rindex("/")] + "/"
        sys.path.append(file_dir)
        print(f"============================== ID_{case_idx} ==============================")
        print("running " + root_path + file_name)
        command = "python " + root_path + file_name
        os.system(command)
