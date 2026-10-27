$taskRoot = $PSScriptRoot
$workRoot = Join-Path $taskRoot '工作区_可清理'
$env:MINERU_HOME = Join-Path $workRoot 'mineru'
$env:MINERU_CONFIG = Join-Path $env:MINERU_HOME 'config.yaml'
$env:HF_HOME = Join-Path $workRoot 'cache\huggingface'
$env:HUGGINGFACE_HUB_CACHE = Join-Path $env:HF_HOME 'hub'
$env:MODELSCOPE_CACHE = Join-Path $workRoot 'cache\modelscope'
$env:TORCH_HOME = Join-Path $workRoot 'cache\torch'
$env:XDG_CACHE_HOME = Join-Path $workRoot 'cache'
$env:PIP_CACHE_DIR = Join-Path $workRoot 'cache\pip'
$env:UV_CACHE_DIR = Join-Path $workRoot 'cache\uv'
$env:TEMP = Join-Path $workRoot 'temp'
$env:TMP = $env:TEMP
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONUTF8 = '1'
$env:HF_HUB_DISABLE_XET = '1'
$env:MINERU_MODEL_SMALL_BACKEND = 'onnx'
$env:GRADIO_ANALYTICS_ENABLED = 'False'
$env:DO_NOT_TRACK = '1'
$env:MINERU_TABLE_DEVICE = 'cpu'
$env:MINERU_INTRA_OP_NUM_THREADS = '4'
$env:MINERU_INTER_OP_NUM_THREADS = '1'
foreach ($taskDir in @($env:MINERU_HOME,$env:HF_HOME,$env:MODELSCOPE_CACHE,$env:TORCH_HOME,$env:PIP_CACHE_DIR,$env:UV_CACHE_DIR,$env:TEMP,(Join-Path $taskRoot '成果'),(Join-Path $taskRoot '进度'))) {
    New-Item -ItemType Directory -Path $taskDir -Force | Out-Null
}
