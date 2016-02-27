
# Mac OS X版のVirtualBox環境の設定

## はじめに

数学的基礎から学ぶ Deep learning (with Python) Vol. 1【MPS 横浜 第1回】

https://mpsamurai.doorkeeper.jp/events/39334

本ドキュメントは、上記イベントで配布されたVirtualBoxの環境において、Mac OS Xで使用するための設定メモです。

## 確認環境

以下の環境で動作確認を行っています。

MacBookAir,
OS X El Capatan
(version 10.11.3)

## VirtualBoxの設定

### 仮想マシンのインポート

配布されたOVAファイルをダブルクリックし、開いたダイアログの「インポート」ボタンを押してください。

***mpsy20160227_default_1456488128503_71141.ova***

### ホストオンリーネットワークを作る

(1) メニューから VirtualBox->環境設定... を選ぶ

(2) ネットワーク->ホストオンリーネットワーク を選ぶ

(3) "vboxnet0"があればそのままで良い。なければ右側の"+"アイコンを押して作成する。

（設定は以下のデフォルトのままでいい）
```
[アダプタ]
IPv4アドレス：192.168.56.1
IPv4ネットマスク：255.255.255.0
IPv6アドレス：（空欄）
IPv6アドレスマスク長：0

[DHCPサーバー]
「サーバーを有効化」のチェックが外れていること
```

（ここでIPv4アドレスが192.168.33.1が指定できれば、Ubuntu側のeth1のIPアドレス変更は不要なのですが）

(4) OKボタンを押して環境設定を終了

これでUbuntuが起動できます。

## Ubuntu環境の整備

Ubuntu環境を起動します。

ログイン名：vagrant

パスワード：vagrant

でログイン。

### 1. 日本語キーボードレイアウトに変更する
　デフォルトでUSキーボードになっています。JISキーボードに変更したい場合、
以下のコマンドを実行してください。

```
$ sudo dpkg-reconfigure keyboard-configuration

（以下を選択）
Apple Aluminium Keyboard (JIS)
Japanese
Japanese
The Default for the keyboard layout
No compose key
```

### 2. eth1のIPアドレスを変更

```
$ sudo vi /etc/network/interfaces

18 auto eth1
19 iface eth1 inet static
20       address 192.168.56.10
21       netmask 255.255.255.0
```
/etc/network/interfacesファイルをviなどで編集します。20行目のaddressを、192.168.33.10から上記のように192.168.56.10に変更してください。

ファイルを保存後、以下のように再起動して変更を更新してください。

```
$ sudo reboot
```

再起動後、ifconfigでeth1のIPアドレスが変更されていることを確認してください。

## jupiterの起動

ログイン後、以下のコマンドを実行してください。

```
$ jupyter notebook
```

Safariから **192.168.56.10:8888** で接続できます。

## その他

### ssh

VirtualBoxでクリップボードの共有設定はあるのですが、どうやらX-Window経由のみでコンソールでは使えないようです。

そこで、Macのターミナルからssh経由でログインして使用することをお勧めします。

```
$ ssh vagrant@192.168.56.10
```
