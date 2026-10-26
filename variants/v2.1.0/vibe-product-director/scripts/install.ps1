[CmdletBinding()]
param(
    [string]$TargetRoot = (Join-Path $HOME '.agents\skills'),
    [switch]$DryRun,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$skillName = 'vibe-product-director'
$sourceDir = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$rootFull = [System.IO.Path]::GetFullPath($TargetRoot)
$homeFull = [System.IO.Path]::GetFullPath($HOME)
$pathRoot = [System.IO.Path]::GetPathRoot($rootFull)
if ($rootFull -eq $pathRoot -or $rootFull -eq $homeFull) {
    throw "Unsafe target root: $rootFull"
}
$targetDir = Join-Path $rootFull $skillName
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupDir = "$targetDir.backup-$stamp"
$stageDir = Join-Path $rootFull ".$skillName.stage-$([guid]::NewGuid().ToString('N'))"

function Test-Package([string]$Path) {
    if (-not (Test-Path -LiteralPath (Join-Path $Path 'SKILL.md') -PathType Leaf)) { return $false }
    if (-not (Test-Path -LiteralPath (Join-Path $Path 'manifest.json') -PathType Leaf)) { return $false }
    $manifest = Get-Content -LiteralPath (Join-Path $Path 'manifest.json') -Raw -Encoding UTF8 | ConvertFrom-Json
    return ($manifest.name -eq $skillName -and $manifest.version -eq '2.1.0')
}

if (-not (Test-Package $sourceDir)) { throw "Source package is not built or valid: $sourceDir" }
if ($DryRun) {
    Write-Output "DRY RUN: install $sourceDir to $targetDir"
    if (Test-Path -LiteralPath $targetDir) { Write-Output "Existing target: overwrite requires -Force and creates $backupDir" }
    exit 0
}

New-Item -ItemType Directory -Path $rootFull -Force | Out-Null
if (Test-Path -LiteralPath $targetDir) {
    $sourceManifest = (Get-FileHash -LiteralPath (Join-Path $sourceDir 'manifest.json') -Algorithm SHA256).Hash
    $targetManifestPath = Join-Path $targetDir 'manifest.json'
    if ((Test-Path -LiteralPath $targetManifestPath) -and ((Get-FileHash -LiteralPath $targetManifestPath -Algorithm SHA256).Hash -eq $sourceManifest)) {
        Write-Output "Already installed: $targetDir"
        exit 0
    }
    if (-not $Force) { throw "A different installation exists at $targetDir. Re-run with -Force to back it up and replace it." }
}

$movedOld = $false
try {
    Copy-Item -LiteralPath $sourceDir -Destination $stageDir -Recurse
    if (-not (Test-Package $stageDir)) { throw "Staged package validation failed: $stageDir" }
    if (Test-Path -LiteralPath $targetDir) {
        Move-Item -LiteralPath $targetDir -Destination $backupDir
        $movedOld = $true
    }
    Move-Item -LiteralPath $stageDir -Destination $targetDir
    Write-Output "Installed to $targetDir"
    if ($movedOld) { Write-Output "Previous installation backed up to $backupDir" }
} catch {
    if ((Test-Path -LiteralPath $stageDir) -and -not (Test-Path -LiteralPath $targetDir)) {
        Move-Item -LiteralPath $stageDir -Destination "$stageDir.failed"
    }
    if ($movedOld -and -not (Test-Path -LiteralPath $targetDir) -and (Test-Path -LiteralPath $backupDir)) {
        Move-Item -LiteralPath $backupDir -Destination $targetDir
    }
    throw
}
