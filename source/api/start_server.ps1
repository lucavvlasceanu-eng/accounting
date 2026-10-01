<#
.SYNOPSIS
    Builds the Docker image, starts the container, pings the endpoint,
    and outputs "OK" on success or container logs on failure.
#>

$ImageName     = "fast-app"
$ContainerName = "fastapi-app"
$Port          = 8080
$Endpoint      = "http://127.0.0.1:${Port}/"

Write-Host "1. Cleaning up previous container..." -ForegroundColor Cyan
docker rm -f $ContainerName *>$null

Write-Host "2. Building Docker image '$ImageName'..." -ForegroundColor Cyan
docker build --no-cache -t $ImageName .

if ($LASTEXITCODE -ne 0) {
    Write-Host "[FAIL] Docker build failed." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "3. Starting container '$ContainerName' on port $Port..." -ForegroundColor Cyan
docker run -d -p "${Port}:${Port}" --name $ContainerName $ImageName *>$null

if ($LASTEXITCODE -ne 0) {
    Write-Host "[FAIL] Docker run failed." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "4. Testing connection to $Endpoint..." -ForegroundColor Cyan

# Give container a couple seconds to fully initialize
$MaxRetries = 5
$RetryCount = 0
$Success    = $false

while ($RetryCount -lt $MaxRetries) {
    Start-Sleep -Seconds 1
    try {
        $Response = Invoke-WebRequest -Uri $Endpoint -UseBasicParsing -TimeoutSec 3 -ErrorAction Stop
        if ($Response.StatusCode -eq 200) {
            $Success = $true
            break
        }
    } catch {
        $RetryCount++
    }
}

Write-Host ""
if ($Success) {
    Write-Host "OK" -ForegroundColor Green
} else {
    Write-Host "[FAIL] Unable to connect. Printing container logs:" -ForegroundColor Red
    Write-Host "--------------------------------------------------" -ForegroundColor DarkGray
    docker logs $ContainerName
    Write-Host "--------------------------------------------------" -ForegroundColor DarkGray
}