import yaml
from pkg_resources import resource_stream


def get_data():
    stream_args = ["suo", "src/data.yaml"]
    stream = resource_stream(*stream_args)
    data = yaml.load(stream, Loader=yaml.FullLoader)
    stream.close()
    return data


def kuo(word, show_all=False):
    data = get_data()
    if word in data.keys():
        if show_all:
            return data[word]
        else:
            return data[word][0]
    else:
        raise ValueError(f"暂未收录：{word}")
