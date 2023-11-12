import json


def edit(filename, key, value):

    def get_new_json(file, key, value):
        key_ = key.split(".")
        key_length = len(key_)
        with open(file, 'rb') as f:
            json_data = json.load(f)
            i = 0
            a = json_data
            while i < key_length:
                if i + 1 == key_length:
                    a[key_[i]] = value
                    i = i + 1
                else:
                    a = a[key_[i]]
                    i = i + 1
        f.close()
        return json_data

    def rewrite_json_file(file, json_data):
        with open(file, 'w') as f:
            json.dump(json_data, f)
        f.close()

    m_json_data = get_new_json(filename, key, value)
    rewrite_json_file(filename, m_json_data)


def read_key(filename, key):

    with open('{0}'.format(filename)) as file:
        data = json.load(file)
        return data['{0}'.format(key)]


def read(filename):
    with open('{0}'.format(filename)) as file:
        data = json.load(file)
        pydata = json.loads(data)
        return pydata


def write(filename, data):

    j = json.dumps(data)
    with open(filename, 'w') as f:
        json.dump(j, f)
