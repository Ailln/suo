from pkg_resources import resource_stream

import yaml


def get_data(data_type="suo"):
    stream_args = ["suo", "src/data.yaml"]
    stream = resource_stream(*stream_args)
    data = yaml.load(stream, Loader=yaml.FullLoader)
    stream.close()

    if data_type == "kuo":
        return data
    elif data_type == "suo":
        new_data = {}
        for key, values in data.items():
            for value in values:
                new_data[value] = key
        return new_data
    else:
        raise ValueError(f"type error: {data_type}")


def suo(word):
    data = get_data("suo")
    if word in data.keys():
        return data[word]
    else:
        raise ValueError(f"暂未收录：{word}")


def kuo(word, show_all=False):
    data = get_data("kuo")
    word = word.lower()
    if word in data.keys():
        if show_all:
            return data[word]
        else:
            return data[word][0]
    else:
        raise ValueError(f"暂未收录：{word}")
