Proxy stuff:
http://swgscanning.ttcg.com:8080 (10.145.250.159)
https://swgscanning.ttcg.com:8443 (10.145.250.159)


**Check setting in powershell:**
Get-ItemProperty -Path "Registry::HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
Get-Variable
Set-variable

**Experiment**
Set-Variable -Name "http_proxy" -value http://vandersw:Waitakere2020!@swgscanning.ttcg.com:8080
Set-Variable -Name "https_proxy" -value https://vandersw:Waitakere2020!@swgscanning.ttcg.com:8443
pip install --proxy=https://vandersw@pgtrust.co.nz:Waitakere2020!@swgscanning.ttcg.com:8443 keyboard

**Powershell:**
$browser = New-Object System.Net.WebClient
$browser.Proxy.Credentials =[System.Net.CredentialCache]::DefaultNetworkCredentials
Invoke-WebRequest https://www.google.com

**Reset by:**
netsh winhttp show proxy
netsh winhttp reset proxy

**Git: Set Proxy:**
git config --global https.proxy http://swgscanning.ttcg.com:8443
git config --global http.proxy http://swgscanning.ttcg.com:8080

**Git: No Proxy:**
git config --global --unset https.proxy
git config --global --unset http.proxy

**Git: Show Proxy details:**
git config --global --get-regexp http.*