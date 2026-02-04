import re
from datetime import datetime, timedelta, timezone

def update_readme():
    # 1. 获取北京时间 (UTC+8)
    tz = timezone(timedelta(hours=8))
    now = datetime.now(tz)
    date_str = now.strftime("%Y.%m.%d")
    
    file_path = 'README.md'
    
    # 2. 读取 README 内容
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 3. 精准匹配 “更新日期：” 后面的日期格式（202x.xx.xx）并替换
    # \d{4} 代表4位数字，\. 代表点号
    new_content = re.sub(r"更新日期：\d{4}\.\d{2}\.\d{2}", f"更新日期：{date_str}", content)
    
    # 4. 写回文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"成功将日期更新为: {date_str}")

if __name__ == "__main__":
    update_readme()