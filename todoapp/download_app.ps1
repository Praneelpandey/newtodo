$release = Invoke-RestMethod -Uri 'https://api.github.com/repos/mobile-next/Milliways/releases/latest'
$asset = $release.assets | Where-Object { $_.name -like '*.ipa' } | Select-Object -First 1

if ($asset) {
    Write-Host "Downloading $($asset.name)..."
    Invoke-WebRequest -Uri $asset.browser_download_url -OutFile "Milliways.ipa"
    Write-Host "Downloaded successfully to Milliways.ipa"
} else {
    Write-Host "No .ipa found in the latest release."
}
