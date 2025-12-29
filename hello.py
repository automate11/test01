from flask import Flask, render_template_string, jsonify

# hello.py
# 简单的个人介绍主页（基于 Flask），在命令行运行：python hello.py

app = Flask(__name__)

profile = {
    "name": "苏妍妍",
    "title": "全栈开发工程师",
    "bio": "热衷于构建简洁、高效的 Web 应用。喜欢学习新技术、解决复杂问题，并把想法变成可用的产品。",
    "skills": ["Python", "Flask", "JavaScript", "React", "SQL", "Docker"],
    "projects": [
        {"name": "个人博客", "desc": "基于 Flask 的静态博客，支持 Markdown 和搜索。", "link": "#"},
        {"name": "任务看板", "desc": "使用 React + Flask 实现的协作任务管理工具。", "link": "#"}
    ],
    "contact": {"email": "you@example.com", "phone": "123-456-7890", "location": "北京, 中国"}
}

TEMPLATE = """
<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{{ name }} - 个人主页</title>
  <style>
    body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; margin:0; padding:0; background:#f6f8fa; color:#111;}
    .container { max-width:900px; margin:36px auto; background:#fff; padding:28px; border-radius:8px; box-shadow:0 6px 24px rgba(20,20,30,0.08);}
    header { display:flex; gap:18px; align-items:center; }
    .avatar { width:96px; height:96px; border-radius:12px; background:linear-gradient(135deg,#6b8cff,#8ee3ff); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:28px; }
    h1 { margin:0; font-size:24px; }
    h2 { margin:18px 0 8px; font-size:18px; color:#333; }
    p { line-height:1.6; color:#444; }
    ul { padding-left:18px; }
    .grid { display:grid; grid-template-columns:1fr 220px; gap:18px; margin-top:18px; }
    .card { background:#fafbff; padding:12px; border-radius:8px; }
    .project { margin-bottom:10px; }
    footer { margin-top:20px; font-size:13px; color:#666; text-align:center; }
    a.button { display:inline-block; padding:8px 12px; background:#2b7cff; color:#fff; border-radius:6px; text-decoration:none; }
    @media (max-width:720px){ .grid{grid-template-columns:1fr;} .avatar{width:76px;height:76px;font-size:22px} }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="avatar">{{ name[0] }}</div>
      <div>
        <h1>{{ name }}</h1>
        <div style="color:#666;">{{ title }}</div>
      </div>
    </header>

    <div class="grid">
      <main>
        <h2>关于我</h2>
        <p>{{ bio }}</p>

        <h2>技能</h2>
        <ul>
        {% for s in skills %}
          <li>{{ s }}</li>
        {% endfor %}
        </ul>

        <h2>项目</h2>
        {% for p in projects %}
          <div class="project card">
            <strong>{{ p.name }}</strong>
            <div style="color:#444;">{{ p.desc }}</div>
            <div style="margin-top:8px;"><a class="button" href="{{ p.link }}" target="_blank">查看</a></div>
          </div>
        {% endfor %}
      </main>

      <aside>
        <div class="card">
          <h2>联系</h2>
          <p>邮箱: <a href="mailto:{{ contact.email }}">{{ contact.email }}</a></p>
          <p>电话: {{ contact.phone }}</p>
          <p>地点: {{ contact.location }}</p>
        </div>

        <div class="card" style="margin-top:12px; text-align:center;">
          <h2>更多</h2>
          <p>导出为 JSON 或通过 API 获取</p>
          <a class="button" href="/api/profile">JSON</a>
        </div>
      </aside>
    </div>

    <footer>生成于本地开发服务器 · 可在 hello.py 中修改资料以定制页面</footer>
  </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(TEMPLATE, **profile)

@app.route("/api/profile")
def api_profile():
    return jsonify(profile)

if __name__ == "__main__":
    # 开发服务器，默认在 localhost:8000
    app.run(host="127.0.0.1", port=8000, debug=True)