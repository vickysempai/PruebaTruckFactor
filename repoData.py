import json
import os
from pydriller import RepositoryMining

def getData():
    try:
        file=open('info.json','r+')
        file.truncate(0)
        file.close()
    except:
        print("Creating File")
    hashes=[]
    data={}
    for commit in RepositoryMining('C:/TEC/VII Semestre/Proyecto/TestPruebaTruckFactor/PruebaTruckFactor').traverse_commits():
        data[commit.hash]=[]
        hashes.append(commit.hash)
        print('\nModificaciones\n')
        for m in commit.modifications:
            x={'author': str(commit.author.name),
            'modified-file':m.filename,
            'type-change':m.change_type.name,
            'differences':m.diff,
            'cyclomatic-complex':m.complexity}
            data[commit.hash].append(x)
            print(
                "Author {}".format(commit.author.name),
                " modified {}".format(m.filename),
                " with a change type of {}".format(m.change_type.name),
                " diff {}".format(m.diff),
                " and the complexity is {}".format(m.complexity))

    with open('info.json','w') as f:
        json.dump(data,f)
    id=1
    for h in hashes:
        os.system("mkdir Commit"+str(h))
        os.system('cd "./Original/PruebaTruckFactor"'+' && git checkout '+ h)
        os.system('Xcopy "./Original" "Commit"'+str(h) +' /y /E /H /C /I')
        id+=1

getData()