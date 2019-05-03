# subtitle translator


srt 字幕翻译软件，翻译功能由谷歌翻译实现。

Translating a subtitle file to any one language, powered by Google Translate.

[Project Home Page](http://coolwp.com/subtitle-translator.html)


## UI

load a srt file

![](screenshot/001.png)

choose a traget language for translation, or it will be simplified-Chinese

![](screenshot/003.png)

translated

![](screenshot/002.png)


## Release

[V1.0.0](https://github.com/suifengtec/subtitle-translator/releases/)


## Source Code

[the initial version code ](./src)

## Softwares Used

```

eric6
Qt Designer


```

## Dependent Python packages
```

pip install PyQt5 fbs requests pysrt  googletrans

```

## Shortcuts

Ctrl+F : Find and open a subtitle file；

Ctrl+T: the current subtitle file will be translate to the selected language, if no language is selected simplified-Chinese by default .

Ctrl+S : save the translated subtitle file;

Ctrl+Alt+S : save as a bilingual subtitle file.


## TODOs

- [x] 自动探测字幕文件原来使用的语种;
- [x] GUI程序;
- [x] 编译为 Windows 上的可安装包;
- [x] 可选择翻译为多个语种中的一种语言;
- [x] 翻译后的字幕文件的重命名方式;
- [x] 保存为新的字幕文件;
- [x] 保存为双语种字幕文件;
- [x] 支持 SubRip (.srt) 类型的字幕文件;
- [] 支持 SubStation Alpha (.ssa)类型的字幕文件;
- [] 支持 WebVTT (.vtt)类型的字幕文件;
- [] 支持 MicroDVD (.sub)类型的字幕文件;
