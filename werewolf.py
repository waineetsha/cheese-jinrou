#!/usr/bin/env python3
import cgi

# ヘッダーを出力
print("Content-Type: text/html\n")

# フォームデータを取得
form = cgi.FieldStorage()

# プレイヤーの投票を取得
player_id = form.getvalue("playerId")

# ここで人狼ゲームのロジックを追加

# レスポンスを出力
print("<html>")
print("<head><title>投票受付完了</title></head>")
print("<body>")
print("<h1>投票を受け付けました！</h1>")
print("<p>投票したプレイヤーID: {}</p>".format(player_id))
print("</body>")
print("</html>")
