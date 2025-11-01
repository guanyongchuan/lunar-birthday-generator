# 🎂 农历生日提醒生成器 · Lunar Birthday ICS Generator

一个可以自动生成未来若干年 **农历生日提醒 .ics 文件** 的在线工具  
支持导入 **Google 日历 / Apple Calendar / Outlook / 手机日历**

✅ 支持选择生成年数（20 / 30 / 40 / 60 年）  
✅ 自动转换农历 → 公历  
✅ 自动添加 3 天前提醒  
✅ ICS 文件可直接导入日历软件  
✅ 界面简洁 · 微信风格按钮  
✅ 可长期使用，不依赖第三方 API  

---

## 🚀 使用方法 · How to Use

1. 进入网站（部署后显示网址）
2. 输入姓名，例如：张三 / Alice
3. 输入农历生日，例如：`8-16`（农历八月十六）
4. 选择生成范围
5. 点击「生成 ICS 文件」并下载
6. 导入到 Google / Apple / Outlook 日历即可

---

## 🛠 本地运行 · Run Locally

```bash
pip install -r requirements.txt
python app.py
