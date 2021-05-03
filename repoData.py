import json
from pydriller import RepositoryMining

def getData():
    try:
        file=open('info.json','r+')
        file.truncate(0)
        file.close()
    except:
        print("Creating File")
    for commit in RepositoryMining('./PruebaTruckFactor').traverse_commits():
        data={}
        data['changes']=[]
        print('\nModificaciones\n')
        for m in commit.modifications:
            x={'author': str(commit.author.name),
            'modified-file':m.filename,
            'type-change':m.change_type.name,
            'differences':m.diff,
            'cyclomatic-complex':m.complexity}
            try:
                with open('info.json') as json_file:
                    data = json.load(json_file)
                    temp=data['changes']
                    temp.append(x)
                with open('info.json', 'w') as outfile:
                    json.dump(data, outfile)
            except:
                try:
                    temp=data['changes']
                    temp.append(x)
                    with open('info.json', 'w') as outfile:
                        json.dump(data, outfile)
                except:
                    temp=data['changes']
                    temp.append(x)
                    with open('info.json', 'x') as outfile:
                        json.dump(data, outfile)
            print(
                "Author {}".format(commit.author.name),
                " modified {}".format(m.filename),
                " with a change type of {}".format(m.change_type.name),
                " diff {}".format(m.diff),
                " and the complexity is {}".format(m.complexity))
getData()