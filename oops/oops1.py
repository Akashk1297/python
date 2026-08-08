avg=0
baseSalary=1000

# define class
class Cricketers:
    def __init__(self,name,playerNo,city,country,role):
        self.name=name
        self.playerNo=playerNo
        self.city=city
        self.country=country
        self.role=role

    def findSalary(self):
        if 'captain' in self.role:
            salary=baseSalary+500
        elif 'vicecaptain' in self.role:
            salary=baseSalary+300
        else:
            salary=baseSalary
        return salary


class Batsman:
    global avg
    def __init__(self,name,id,matches,runs,role):
        self.id=id
        self.name=name
        self.matches=matches
        self.runs=runs
        self.role=role

    def findAverage(self):
        if 'batsman' in self.role:
            avg=runs//matches
        else:
            print('Cricketer is not batsman.')

        return avg

n=int(input('enter no of cricketers: '))

for i in range(n):
    # take input from user
    name=(input('enter name of cricketer: '))
    playerNo=int(input('enter player number: '))
    city=(input('enter city: '))
    country=(input('enter country: '))
    role=input('enter role: ').split()

    #  Logic check
    if 'captain' in role and 'vicecaptain' in role:
        raise ValueError('Both captain and vicecaptain roles not allowed for same person.')
    else:
        print('Role entered is ok.')

    # create object
    p=Cricketers(name,playerNo,city,country,role)

    # display attributes
    print('name: ',name)
    print('playerNo: ',playerNo)
    print('city',city)
    print('country: ',country)
    print('role: ',role)
    print('Salary: ',p.findSalary())


print('\n Enter details of batsman ?')
name=(input('enter name of batsman: '))
playerNo=int(input('enter player number: '))
matches=int(input('enter matches: '))
runs=int(input('enter runs: '))
b1=Batsman(name,playerNo,matches,runs,'batsman')
print('Batting average of Player name: ',b1.name, ' is: ',b1.findAverage())
