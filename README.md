# SUO

🦩中英文缩写转化

## 1 功能

- suo.kuo: 扩写
- suo.suo: 缩写 # 开发中

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
cd suo
python setup.py install
```

## 3 使用

### 3.1 扩写

1. 获得扩写

```bash
from suo import kuo
result = kuo("awsl")
print(result)
# "阿伟死了"
```

2. 获得所有可能的扩写

```bash
from suo import kuo

result = kuo("awsl", show_all=True)
print(result)
# ["阿伟死了", "啊我死了']
```

## 4 许可

[![](https://award.dovolopor.com?lt=License&rt=MIT&rbc=green)](./LICENSE)

## 5 参考

- [如何从模板创建仓库？](https://help.github.com/cn/articles/creating-a-repository-from-a-template)
- [如何发布自己的包到 pypi ？](https://www.v2ai.cn/python/2018/07/30/PY-1.html)
