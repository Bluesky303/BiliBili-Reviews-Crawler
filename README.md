通过给定关键词列表，在不同时间段按评论数顺序分别进行搜索，依据bv号合并同一时间段视频信息，同关键词不同时间在同一个xlsx不同sheet中。


然后根据bv号列表进行搜索，按默认排序获取需要页数的一级评论数，合并评论后去除表情信息，写入txt文件


使用结巴(jieba)中文分词库，对评论进行关键词分析并且基于wordcloud做成词云图，同时生成词频json和txt文件


以后可能会做的：
1.加ui
2.评论获取量较大时会被b站封ip，需要建立暂停和缓存方法

本项目参与人大竞赛http://youth.ruc.edu.cn/ggl/f78e3127bc51418097f64a8ba33fc87f.htm


# 用于获取b站评论的

打包命令
pyinstaller --onefile --add-data "crawler/resources/**/*;crawler/resources/" --noconsole main.py