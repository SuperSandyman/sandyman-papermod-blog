---
date: "2022-12-15"
title: "Flatpakを使ってUbuntuにChromeをインストールする"
thumbnail: "images/chrome.webp"
tags: ["Chrome", "Linux", "Flatpak"]
categories: ["Linux"]
archives: ["2022/12"]
toc: true
aliases: ["/flatpak-chrome-install"]
---

## はじめに

私が普段使っているブラウザは Firefox なのですが、グリーンチャンネル Web で香港国際競走を見ようとしたらなんと Firefox に対応してませんでした！！これは大変だ！ということで、急遽レース開始の 7 分前くらいに Chrome をインストールすることになったのですが、結構戸惑ったのでメモを残しておきます。

## 実施環境

- Kubuntu 22.04.1 (Kubuntu と Ubuntu はほぼ同じ)
- Linux 5.15
- ThinkPad X1 Carbon Gen10

## Flatpak でインストール

Google 公式から deb ファイルを落としてインストールすることもできたらしいのですが、Snap 版 Firefox の仕様でなぜかダウンロードリンクが表示されなかったので、Flatpak でインストールすることにしました。

## Flatpak を導入しよう

まずは Flatpak を導入します。インストールのコマンドはこれです。

```
sudo apt install flatpak
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

実行し終わったら、念の為再起動しておきます。

## Chrome をインストールする

それでは、Chrome をインストールしていきます。下のコマンドで Chrome をインストールしていきます。

```
flatpak install flathub com.google.Chrome
```

インストールには少し時間がかかるので焦らず待ちましょう。インストールが終わったらどっかに追加されているはずです。これで競馬が見れますね！！~~あれもうレースはじまってる...~~

## まとめ

ということで、今回は Chrome をインストールしてみました！他にも Flatpak でいろいろなソフトをインストールできるのでぜひ使ってみてください。ソフトウェアについてはここから見れます！[https://flathub.org/home](https://flathub.org/home)

それではさようならー！！
