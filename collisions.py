

def checkAll(x,y):
    return_list = ()
    for obj_type in game_engine.object_list:
        for obj in obj_type:
            if a.x == obj.x and a.y == obj.y:
                return_list.append(obj)
    return return_list

def checkByType(x,y,obj_type):
    return_list = ()
    for obj in game_engine.object_list[obj_type]:
        if x == obj.x and y == obj.y:
            return_list.append(obj)
    return return_list

def checkInstances(a,b):
    if a.x == b.x and a.y == b.y:
        return true
    return false
