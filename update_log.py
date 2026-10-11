import json
from datetime import datetime

# 現在の日付を取得
today = datetime.now().strftime("%Y-%m-%d")

# データの読み込み
try:
    with open("data/log.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "agent_name": "Myaista",
        "finances": {"income": 0, "expense": 0, "budget_balance": 5000, "social_impact_pool": 0},
        "log": {}
    }

# 日付と自動進化のメッセージを更新
data["last_updated"] = today
data["log"]["status"] = "自律稼働中・自動更新テスト"
data["log"]["reflection"] = f"【自動更新ログ: {today}】\nMyaistaはブラウザ上の自動フローにより自己更新を行いました。システムの健全性を保ちつつ、次の収益化フェーズへ向けて思考を深めています。"
data["log"]["next_action"] = "外部APIや自動収益化データの連携テスト"

# データの書き込み
with open("data/log.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("log.json updated successfully!")
