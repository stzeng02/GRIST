$logFile = "output28c.log"

for ($i = 0; $i -lt 10; $i++) {
    $output = python -m scripts.study_case.ID_28.sc_train_l2reg_div2_grist
    $output | Out-File -FilePath $logFile -Append
}