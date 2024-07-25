# ibus_rime_flypy
* 设置是, 事, 时, 十的编码u, ui, uio, uial/eu;
* 设置Ctrl+空格切换中英文模式, 配合ubuntu默认的super+space切换语言输入法与win10体验一致.
* 添加咲, 氷, 畑, 栞, 姦, 雫等常用字.
* 添加常用符号快捷键opi π
* 添加线程, 控件, 服务器, 枚举, μ's, 哆啦, 哆啦A梦, 矢泽妮可等常用词汇.
* 删除老妈子, 曲直等不常用词汇
* 拼音字符支持ofpya ofpyo等方式快速检索
* 增加反查编码支持, 按`` ` ``开始检索. 在输入过程中也可以按`` ` ``代替任意字符检索. 仅支持检索字, 不能检索词.
* 在dict添加汉字后, 在wc.txt中添加全码, 运行getwc.py即可自动更新反查字典. 添加词不需要更新
> 官方的小鹤输入法支持Windows, Android, Macos与Ios, 此版本仅支持Linux, 其他平台未验证, 建议使用官方版本. 词库为早期公开版本修改而来, 不随官方版本更新. 输入法本身基于10.7版本配置修改, 词库与该版本无关.
> ubuntu或debian可以直接使用deb安装包, 但不建议, deb更新缓慢
# 手动安装
安装ibus-rime后在~/.config/ibus文件夹中执行git clone https://github.com/walterclozet/ibus_rime_flypy.git rime
重新部署即可
# 更新
cd ~/.config/ibus/rime
git pull 
