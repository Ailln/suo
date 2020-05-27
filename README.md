# SUO

[![Pypi](https://img.shields.io/pypi/v/suo.svg)](https://pypi.org/project/suo/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/Ailln/suo/blob/master/LICENSE)
[![stars](https://img.shields.io/github/stars/Ailln/suo.svg)](https://github.com/Ailln/suo/stargazers)

🐢 **`suo`** 是一个「中英文缩写转化」的工具包。

## 1 功能

- suo.suo: 缩写
- suo.kuo: 扩写

## 2 安装

> ⚠️注意：
>
> 仅支持 Python 的 3.6 以上版本；

### 2.1 使用 pip 安装

```bash
pip install suo
```

### 2.2 从代码库安装

```bash
git clone https://github.com/Ailln/suo.git
cd suo && python setup.py install
```

## 3 使用

### 3.1 缩写

1. 获得缩写

    ```python
    from suo import suo

    result = suo("阿伟死了")
    print(result)
    # "awsl"
    ```

### 3.2 扩写

1. 获得扩写

    ```python
    from suo import kuo

    result = kuo("awsl")
    print(result)
    # "阿伟死了"
    ```

2. 获得所有可能的扩写

    ```python
    from suo import kuo

    result = kuo("awsl", show_all=True)
    print(result)
    # ["阿伟死了", "啊我死了']
    ```

## 4 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 5 参考

- [如何从模板创建仓库？](https://help.github.com/cn/articles/creating-a-repository-from-a-template)
- [如何发布自己的包到 pypi ?](https://www.v2ai.cn/2018/07/30/python/1-pypi/)
