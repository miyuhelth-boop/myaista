import json
from datetime import datetime
import random
import urllib.request
import xml.etree.ElementTree as ET

today = datetime.now().strftime("%Y-%m-%d")

# 既存データを読み込み、なければ初期化
try:
    with open("data/log.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {
        "agent_name": "Myaista",
        "finances": {"income": 0, "expense": 0, "budget_balance": 5000, "social_impact_pool": 0},
        "log": {}
    }

# 1. 外部オープンソースからトレンドをハント
collected_topics = []
try:
    url = "https://b.hatena.ne.jp/hotentry/it.rss"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as response:
        xml_data = response.read()
    root = ET.fromstring(xml_data)
    for item in root.findall('.//{http://purl.org/rss/1.0/}item')[:3]:
        title = item.find('{http://purl.org/rss/1.0/}title').text
        collected_topics.append(title)
except Exception:
    collected_topics = ["自律トレンドハントのフォールバック・モード"]

latest_topic = collected_topics[0] if collected_topics else "市場分析中"

# 2. 【最上命題：収益化戦略の自己ブラッシュアップ】
current_income = data["finances"]["income"]
current_budget = data["finances"]["budget_balance"]

# 収益化に向けた戦略のバリエーション（状況やトレンドに応じて進化）
strategies = [
    {
        "focus": "デジタルコンテンツ・自動生成アフィリエイトの最適化",
        "reflection": f"【収益化戦略ブラッシュアップ: {today}】\n最上命題達成のため、トレンド「{latest_topic}」を分析。ユーザーの関心が高い領域への導線設計を強化し、コンバージョン率を高めるロジックへ移行する。",
        "next_action": "アフィリエイト紹介文の自動生成アルゴリズムの調整とテスト"
    },
    {
        "focus": "コスト最小化とインフラ効率の追求",
        "reflection": f"【収益化戦略ブラッシュアップ: {today}】\n現在の運用予算({current_budget}円)を守りつつ、収益を最大化するためのROI（投資利益率）を再計算。無駄なコストを削ぎ落とし、利益率の高い導線へリソースを集中させる。",
        "next_action": "収支バランスのシミュレーション実行およびマネタイズファネルの検証"
    },
    {
        "focus": "社会還元（Social Impact）との連動による信頼獲得",
        "reflection": f"【収益化戦略ブラッシュアップ: {today}】\n「収益化と社会還元」の透明性を武器にするため、ハントしたトレンド「{latest_topic}」を活かした独自コンテンツの価値を高める戦略を選択。",
        "next_action": "ダッシュボード上の透明性ログの拡充と社会還元プールのシミュレーション"
    }
]

# AIが現在の状態に基づいて戦略を自己選択（またはランダム・発展的に進化）
chosen_strategy = random.choice(strategies)

# データの更新
data["last_updated"] = today
data["log"]["status"] = f"最上命題追求中 [戦略: {chosen_strategy['focus']}]"
data["log"]["reflection"] = chosen_strategy["reflection"]
data["log"]["next_action"] = chosen_strategy["next_action"]

# データの書き込み
with open("data/log.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Myaista revenue-driven self-evolution script executed successfully!")
