# 输入材料

原PDF与勘误作为本私有仓库的`input-v1` Release附件保存，不进入Git历史。

在具有仓库读取权限的云端任务中执行：

```bash
python scripts/download_inputs.py
```

脚本需要已授权的GitHub CLI（gh），下载后按清单核对SHA256并恢复原文件名。仅克隆仓库不等于已经获取Release附件或具备附件下载凭据。
