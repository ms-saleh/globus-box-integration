globus login
globus whoami
Set-Variable -Name "aps_id" -Value e133a81a-6d04-11e5-ba46-22000b92c6ec
Get-Variable -Name "aps_id"
Set-Variable -Name "my_id" -Value fbe89660-0fe5-11ec-90b6-41052087bc27
Get-Variable -Name "my_id"
#globus ls -F json $aps_id":/2-BM/2021-07/Sobhani_corr/tomography_corr" > tomography.json
#globus ls -r -F json $aps_id":/2-BM/2021-07/Sobhani" > Sobhani.json
globus ls -F json $aps_id":/2-BM/2021-07/Sobhani_corr/radiography_corr" > radiography.json
# python listDir.py "tomography.json"
python listDir.py "radiography.json"
# python listDir.py "Sobhani.json"