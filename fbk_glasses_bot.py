import praw

reddit = praw.Reddit(
    user_agent="fbk_glasses_bot (by u/yoyoyonono)",
    client_id="redacted",
    client_secret="redacted",
    username="redacted",
    password="redacted"
)

fbk_copypasta = """I gotchu
_Takes a deep breath_

Glasses are really versatile. First, you can have glasses-wearing girls take them off and suddenly become beautiful, or have girls wearing glasses flashing those cute grins, or have girls stealing the protagonist's glasses and putting them on like, "Haha, got your glasses!" That's just way too cute! Also, boys with glasses! I really like when their glasses have that suspicious looking gleam, and it's amazing how it can look really cool or just be a joke. I really like how it can fulfill all those abstract needs. Being able to switch up the styles and colors of glasses based on your mood is a lot of fun too! It's actually so much fun! You have those half rim glasses, or the thick frame glasses, everything! It's like you're enjoying all these kinds of glasses at a buffet. I really want Luna to try some on or Marine to try some on to replace her eyepatch. We really need glasses to become a thing in hololive and start selling them for HoloComi. Don't. You. Think. We. Really. Need. To. Officially. Give. Everyone. Glasses?


_this is a bot. by u/yoyoyonono_"""

fbk_copypasta_jp = """I gotchu
_Takes a deep breath_

眼鏡っていうのは本当にめちゃめちゃ多様性があるんですよねまず眼鏡をかけている女の子が眼鏡を外して美少女だったりとか逆に眼鏡をかけてニコニコしてみたり主人公の眼鏡を奪って着けてる女子や｢うばっちゃったぞ☆｣みたいにかけてそれも凄いかわいいんですよねあとは眼鏡男子もねあの眼鏡があやしく光ったり逆光してる姿もいいですしかっこいいもかわいいもそしてギャグまで使い回せるってのはめちゃめちゃいいんですよねシチュエーションでも対応してできるところもめちゃめちゃいいんですよ多種多様な形とか色とかもそのキャラに合った眼鏡を着せ替えて楽しむのも本当に楽しいですアンダーリムとかねちょっと淵が太いやつとかね本当にヴァイキングのようにめちゃめちゃ楽しめるんですルーナちゃんにかけてみたりマリンちゃんも眼帯外してかけてみたりとかもうホロライブメガネはマジで流行ってほしいしホロコミに出すべきだし是非！公式から！みんなに！眼鏡を！付与して！ほしいと思わないかなぁ！？かけたいよね？


_this is a bot. by u/yoyoyonono_"""
glasses = 'glasses'
glasses_type_japanese_words = ['megane', '眼鏡', 'メガネ', 'めがね']

subreddit = reddit.subreddit("hololive+hololewd+test")
while True:
    try:
        for submission in subreddit.stream.submissions():
            print(submission.title)
            if glasses in ''.join(e for e in submission.title.lower() if e.isalnum()):
                try:
                    print('replied')
                    submission.reply(fbk_copypasta)
                except:
                    print('rate limited')
                continue
            else:
                for x in glasses_type_japanese_words:
                    if x in ''.join(e for e in submission.title.lower() if e.isalnum()):
                        try:
                            print('replied')
                            submission.reply(fbk_copypasta_jp)
                        except:
                            print('rate limited')
                        continue
    except:
        pass

