$logFile = "output_cifar_61.log"

for ($i = 0; $i -lt 10; $i++) {
    $output = python -m scripts.study_case.CIFAR_10_61.multi_layer_perceptron_grist
    $output | Out-File -FilePath $logFile -Append
}