#!/usr/bin/env python3
import cgi
import random

# ヘッダーを出力
print("Content-Type: text/html\n")

# フォームデータを取得
form = cgi.FieldStorage()

# ゲームの設定
players = ["ねぼすけネズミ"] * 5  # プレイヤー数は仮の値です
cheese_robber_index = random.randint(0, len(players) - 1)
players[cheese_robber_index] = "チーズドロボー"

# ゲームの進行
# チーズドロボーが盗む関数
def steal_cheese():
    print("<p>夜が明けました。ねぼすけネズミたちが目を覚まし、チーズを確認します...</p>")
    if players[cheese_robber_index] == "チーズドロボー":
        print("<p>チーズドロボーはチーズを盗みました！</p>")
    else:
        print("<p>今夜はチーズドロボーは現れませんでした。</p>")

# メインのHTMLコンテンツ
print("<html>")
print("<head><title>チーズは誰が食べた？</title></head>")
print("<body>")
print("<h1>チーズは誰が食べた？</h1>")

# 夜のフェーズ
print("<h2>夜</h2>")
print("<p>全員で目を閉じてください...</p>")
steal_cheese()

# 昼のフェーズ
print("<h2>昼</h2>")
print("<p>みんなで話し合いましょう！</p>")
print("<p>誰がチーズドロボーか推理しましょう。</p>")
print("<p>投票してください：</p>")
for index, player in enumerate(players):
    print('<input type="radio" name="vote" value="{}" id="player{}">'.format(player, index))
    print('<label for="player{}">{}</label><br>'.format(index, player))
print('<button onclick="submitVote()">投票する</button>')

# 投票結果を処理するスクリプト
print("""
<script>
function submitVote() {
    var selectedPlayer = document.querySelector('input[name="vote"]:checked');
    if (selectedPlayer) {
        alert("投票しました！" + selectedPlayer.value + "に投票しました。");
        // ここでフォームを送信するなどの処理を行う
    } else {
        alert("プレイヤーを選択してください！");
    }
}
</script>
""")

print("</body>")
print("</html>")
