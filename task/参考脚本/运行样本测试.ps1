param([string]$Only = '')
$ErrorActionPreference = 'Stop'
. (Join-Path $PSScriptRoot 'env.ps1')
$env:MINERU_MODEL_SOURCE = 'local'
$env:HF_HUB_OFFLINE = '1'
$taskPython = Join-Path $PSScriptRoot '工作区_可清理\venv\Scripts\python.exe'
if ($Only) {
    & $taskPython (Join-Path $PSScriptRoot 'run_samples.py') --only $Only
} else {
    & $taskPython (Join-Path $PSScriptRoot 'run_samples.py')
}
if ($LASTEXITCODE -ne 0) { throw "样本解析失败，查看进度日志与sample-status.json。" }
& $taskPython (Join-Path $PSScriptRoot 'export_test_results.py')
if ($LASTEXITCODE -ne 0) { throw '测试结果导出失败。' }
