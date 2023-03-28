import subprocess

num = int(input("通常記事を作成する場合は1を、Scrapsを作成する場合は2を、投稿するときは3を入力してください。>>>"))

if num == 1:
    post_name = str(input("記事のslugを入力してください。>>>"))
    subprocess.run(["hugo", "new", f"posts/{post_name}/index.md"])
    print("記事を作成しました。")
elif num == 2:
    scraps_name = str(input("Scrapsのslugを入力してください。>>>"))
    subprocess.run(["hugo", "new", f"scraps/{scraps_name}/index.md"])
    print("Scrapsを作成しました。")
elif num == 3:
    commit_message = str(input("コミットメッセージを入力してください。>>>"))
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])
    subprocess.run(["git", "push", "-u", "origin", "main"])
else:
    print("1か2か3を入力してください。")
