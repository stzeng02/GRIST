$logFile = "output_cifar_7.log"

for ($i = 0; $i -lt 10; $i++) {
    $output = python -m scripts.study_case.CIFAR_10_7.soips2_grist
    $output | Out-File -FilePath $logFile -Append
}