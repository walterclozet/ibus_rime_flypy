# ibus_rime_flypy
* 设置是, 事, 时, 十的编码u, ui, uio, uial/eu;
* 设置Ctrl+空格切换中英文模式, 配合ubuntu默认的super+space切换语言输入法与win10体验一致.
* 添加咲, 氷, 畑, 栞, 姦, 雫等常用字.
* 添加常用符号快捷键opi π
* 添加线程, 控件, 服务器, 枚举, μ's, 哆啦, 哆啦A梦, **矢泽妮可**等常用词汇.
* 删除老妈子, 曲直等不常用词汇
* 拼音字符支持ofpya ofpyo等方式快速检索
* 增加反查编码支持, 按`` ` ``开始检索. 在输入过程中也可以按`` ` ``代替任意字符检索. 仅支持检索字, 不能检索词.
* 在dict添加汉字后, 在wc.txt中添加全码, 运行getwc.py即可自动更新反查字典. 添加词不需要更新
* 添加日语假名快捷键, 作为用户词库, 可选
> 官方的小鹤输入法支持Windows, Android, Macos与Ios, 此版本仅支持Linux, 其他平台未验证, 建议使用官方版本. 词库为早期公开版本修改而来, 不随官方版本更新. 输入法本身基于10.7版本配置修改, 词库与该版本无关.
> ubuntu或debian可以直接使用deb安装包, 但不建议, deb更新缓慢
# 手动安装
安装ibus-rime后在~/.config/ibus文件夹中执行git clone https://github.com/walterclozet/ibus_rime_flypy.git rime
重新部署即可
# 更新
cd ~/.config/ibus/rime
git pull 
# Windows 手动安装
安装小狼毫后, 打开用户文件夹, 下载最新代码解压后将所有文件复制到此重新部署即可.
更新时重新下载压缩包解压覆盖已有文件, 重新部署.
也可安装git后执行git clone, git pull, 与linux方法相同.
# 假名快捷键
あ	cha

い	chi

う	chu

え	che

お	cho

ア	cha

イ	chi

ウ	chu

エ	che

オ	cho

か	chka

き	chki

く	chku

け	chke

こ	chko

カ	chka

キ	chki

ク	chku

ケ	chke

コ	chko

さ	chsa

し	chui

す	chsu

せ	chse

そ	chso

サ	chsa

シ	chui

ス	chsu

セ	chse

ソ	chso

た	chta

ち	chii

つ	chiu

て	chte

と	chto

タ	chta

チ	chii

ツ	chiu

テ	chte

ト	chto

な	chna

に	chni

ぬ	chnu

ね	chne

の	chno

ナ	chna

ニ	chni

ヌ	chnu

ネ	chne

ノ	chno

は	chha

ひ	chhi

ふ	chhu

へ	chhe

ほ	chho

ハ	chha

ヒ	chhi

フ	chhu

ホ	chho

ま	chma

み	chmi

む	chmu

め	chme

も	chmo

マ	chma

ミ	chmi

ム	chmu

メ	chme

モ	chmo

や	chya

ゆ	chyu

よ	chyo

ヤ	chya

ゆ	chyu

よ	chyo

ら	chra

り	chri

る	chru

れ	chre

ろ	chro

ラ	chra

リ	chri

ル	chru

レ	chre

ロ	chro

わ	chwa

ワ	chwa

を	chwo

ヲ	chwo

ん	chn

ン	chn

ぱ	chpa

ぴ	chpi

ぷ	chpu

ぺ	chpe

ぽ	chpo

パ	chpa

ピ	chpi

プ	chpu

ペ	chpe

ポ	chpo

が	chga

ぎ	chgi

ぐ	chgu

げ	chge

ご	chgo

ざ	chza

じ	chji

ず	chzu

ぜ	chze

ぞ	chzo

だ	chda

ぢ	chji

づ	chzu

で	chde

ど	chdo

ば	chba

び	chbi

ぶ	chbu

べ	chbe

ぼ	chbo

ガ	chga

ギ	chgi

グ	chgu

ゲ	chge

ゴ	chgo

ザ	chza

ジ	chji

ズ	chzu

ゼ	chze

ゾ	chzo

ダ	chda

ヂ	chji

ヅ	chzu

デ	chde

ド	chdo

バ	chba

ビ	chbi

ブ	chbu

ベ	chbe

ボ	chbo

ゃ	chva

ゅ	chvu

ょ	chvo

ャ	chva

ュ	chvu

ョ	chvo

っ	chvs

ッ	chvs

ィ	chvi


