# 第一章（计算机基础）

本章学习以下内容

1. Git的使用
2. Github的使用
3. APIFox的了解
4. python环境搭建
5. node环境搭建
6. shell的基本使用
7. Windows terminal安装
8. vscode安装配置
9. jetbrains的安装配置

## 任务一：Git的使用

### 任务点

1. 安装git
2. 使用git进行版本管理。需要使用以下功能
   1. git add
   2. git commit
   3. 回退到某一次提交
   4. 创建分支
   5. 删除分支
   6. 回退某一个文件
   7. 合并分支

### 资料

https://rogerdudler.github.io/git-guide/index.zh.html

### 提交文件

- 以下文件放置在 `task1` 文件夹下
- 用来记录安装过程笔记文件 `git_install.md`
- 一张用来记录安装成功的截图 `git.jpg`
- 使用git进行版本管理的过程文档 `git.md`

## 任务二：Github的使用

- Github地址：https://github.com/
- 工作室空间：https://github.com/TickNet-Hnust/
- 此仓库地址：https://github.com/TickNet-Hnust/ticknet2022/

### 任务点

1. 浏览GitHub，使用GitHub高级搜索功能，找到几个你感兴趣的仓库，并阅读其README介绍，了解改仓库。
2. 尝试发布任务一所创建的本地仓库到GitHub
3. 为你上传到GitHub上的仓库提出一个issue
4. 为你上传到GitHub上的仓库提交一个pr
5. 为你上传到GitHub上的仓库合并一个pr

### 提交文件

- 以下文件放置在 `task2` 文件夹下
- 记录过程文档 `github.md` ，需要包含以下几点
    - GitHub仓库地址
    - 过程描述
    - 问题以及解决方法

## 任务三：环境安装

### 任务点

1. 安装APIFox并熟悉
2. 安装nodejs
3. 安装python
4. Windows Terminal安装（推荐但是不必须）
5. vscode安装配置
6. jetbrains的安装配置

### 提交文件

- 以下文件放置在 `task3` 文件夹下
- `env.md` 文件用来记录过程需要包括以下几点
    - 安装结果展示
    - 问题以及解决方法

## 任务四：shell的基础操作

## 资料

- https://archlinuxstudio.github.io/ShellTutorial/#/
- https://www.runoob.com/linux/linux-shell.html

### 任务点

- 熟悉shell基本操作

### 提交文件

- 以下文件放置在 `task4` 文件夹下
- `shell.md` 用来记录学习过程

## 提交

对于上面的每一小节，都有自己的文件夹 `task0`、 `task1` 等等。

我们还要求你编写文档来记录本章学习过程，可以是以博客的样式记录。把文档写入到 `submit.md` 中即可，该文件会在运行提交命令后自动上传。

此时你的工作目录应该是这样子的

![img.png](imgs/img.png)

打开`submit.yml`填入`secret key`到`key`键中。这被我们用来标识你的身份。

将你的代码交予git管理，这样在切换分支的时候修改不会丢失。

```shell
# 添加到暂存区
git add .
# 提交
git commit -m "<一些描述信息>"
```

然后将你想要提交的文件添加到 `submit.yml` 的 `upload_files` 键下。**请勿删除原有的项目**。例如如果想要添加 `install.sh` 则添加成这个样子

```yaml
upload_files:
  - "submit.md"
  - "install.sh"
  # - "*.sh" 使用通配符匹配所有以 `.sh` 结尾的文件
  # - "folder" 或者上传一个文件夹
```

最后运行以下命令提交。

```shell
python submit.py
```
