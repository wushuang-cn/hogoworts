import yaml


def get_yamldatas(key,type='datas'):
    #datas=yaml.safe_load(open("../Datas/data1.yml"))
    with open("../Datas/data1.yml") as f:
        datas=yaml.safe_load(f)

    return datas[key][type]

if __name__=='__main__':
    print(get_yamldatas('add'))
    print(get_yamldatas('add','ids'))
