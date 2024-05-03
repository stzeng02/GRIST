$logFile = "output_cifar_24.log"

for ($i = 0; $i -lt 10; $i++) {
    $output = python -m scripts.study_case.CIFAR_10_24.Mnist_grist
    $output | Out-File -FilePath $logFile -Append
}