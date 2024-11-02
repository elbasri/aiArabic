

task = {'id': 1, 'title': 'arabic ai', "done": True}
print(task)
task2 = dict([('id', 1 ), ('title', "arabic ai"), ('done', True)])
print(task2)

print(task['id'])
print(task2['title'])

mowaddafin = {1: "Nacer", 2:"Mohamed", 3:"Hicham", 4:"Basma"}
print(mowaddafin[1])

task['done'] = False
print(task['done'])

print("id" in task)
print("email" in task)

print(len(mowaddafin))

print(task.get('title'))

taskKeys = task.keys()
print(taskKeys)

task.update({'email': 'devnasser@gmail.com'})
print(task.values())

