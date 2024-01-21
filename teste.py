'''def dir_reduc(arr):
    opostos={"NORTH":"SOUTH","SOUTH":" NORTH","EAST":"WEST","WEST":"EAST"}
    nova_rota=[]
    for d in arr:
        if nova_rota and nova_rota[-1]== opostos[d]:
            nova_rota.pop()
        else:
            nova_rota.append(d)
    return print(nova_rota)'''
    
    
    
def dir_reduc(plan):
    opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return print(new_plan)    
dir_reduc (["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])       