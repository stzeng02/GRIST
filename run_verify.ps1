$logFile = "output_cifar_63.log"

for ($i = 0; $i -lt 10; $i++) {
    $output = python -m scripts.study_case.CIFAR_10_63.main_grist
    $output | Out-File -FilePath $logFile -Append
}