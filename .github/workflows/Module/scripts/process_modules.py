import urllib.request
import os

# 定义上游源地址与本地保存路径的映射
modules = {
    "wloc.sgmodule": "https://raw.githubusercontent.com/Yu9191/wloc/refs/heads/main/modules/wloc.module",
    "TikTok-Unlock.sgmodule": "https://raw.githubusercontent.com/Semporia/TikTok-Unlock/master/Shadowrocket/TikTok.sgmodule"
}

output_dir = "Module/Expansion Module/Sync"
os.makedirs(output_dir, exist_ok=True)

for filename, url in modules.items():
    print(f"Fetching {url}...")
    req = urllib.request.urlopen(url)
    content = req.read().decode('utf-8')
    
    # ==========================================
    # 在这里进行你需要的“修改/整理”逻辑
    # ==========================================
    # 示例1：替换或抹掉上游的特定注释
    content = content.replace("by Yu9191", "by AIX-Open") 
    
    # 示例2：强制将某些策略组重定向为你统一的代理组
    # content = content.replace("旧代理组名", "PROXY")
    
    # 保存到本地仓库
    file_path = os.path.join(output_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully processed and saved to {file_path}")
