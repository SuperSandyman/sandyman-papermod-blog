---
date: "2022-09-16"
title: "CSSフレームワーク「Bulma」でいろいろ作ってみた"
thumbnail: "images/cooldevelop.webp"
tags: ["Bulma", "CSS", "デザイン"]
categories: ["CSS"]
archives: ["2022/09"]
aliases: ["/css-bulma-using"]
---

## はじめに

皆さんこんにちは！Sandy マンです！

今回は、CSS フレームワークである「Bulma」を使って実際にいろいろ作ってみたいなと思います！それではやっていきます！

## Bulma とは

そもそも Bulma とはどのようなフレームワークなのでしょうか。公式サイトにはこんなことが書いてあります。

> Bulma is a free, open source framework that provides ready-to-use frontend components that you can easily combine to build responsive web interfaces.

要は、「簡単にレスポンシブ対応の UI を構築できるよー」みたいなそんな感じです。それでは早速使ってみましょう！

## Bulma を導入する

### CDN を利用する場合

CDN を利用する場合は、次のコードを HTML の Head タグ内に埋め込みます。

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css"
/>
```

### npm パッケージを利用する場合

npm パッケージを利用する場合は、次のコマンドを実行します。

```
npm install bulma
```

（yarn の場合）

```
yarn add bulma
```

## Bulma でいろいろ作ってみる

### ボタン

ボタンはこんな感じで作れました！全体的にパステルカラーといった感じで、きれいにまとまっていますね。
{{< codepen supersandyman RwypPYW >}}

### ヘッダー

ヘッダーはこんな感じです！nav タグの"is-dark"というクラスを消せばライトモードにもできます。しっかりレスポンシブ対応していていいですね！
{{< codepen supersandyman jOxBbOx >}}

### プログレスバー

プログレスバーも作ってみました！すごく派手ですね！
{{< codepen supersandyman yLjMPrd >}}

## まとめ

ということで、Bulma でいろいろ作ってみました！実はここまで紹介したものは全て、公式ドキュメントのコードをアレンジしたものだったりします。他にもいろいろ実装例が紹介されているので、ぜひ公式ドキュメントも見てみてください！それではさようならーーーー！！

公式ドキュメントはこちらから...
[bulma.io/documentation](https://bulma.io/documentation)
