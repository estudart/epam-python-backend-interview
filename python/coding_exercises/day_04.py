import time

"""
grid = ['uxf', 'vof', 'hmp']


def gridChallenge(grid):
    def is_sorted(string: str):
        return string == "".join(sorted(string))  

    sorted_grid =[]
    for row in grid:
        sorted_row = "".join(sorted(row))
        sorted_grid.append(sorted_row)

    for i in range(len(grid[0])):
        if is_sorted("".join([item[i] for item in sorted_grid])):
            continue
        else:
            return "NO"
    return "YES"

print(gridChallenge(grid))
"""

"""
n = '7404954009694227446246375747227852213692570890717884174001587537145838723390362624487926131161112710589127423098959327020544003395792482625191721603328307774998124389641069884634086849138515079220750462317357487762780480576640689175346956135668451835480490089962406773267569650663927778867764315211280625033388271518264961090111547480467065229843613873499846390257375933040086863430523668050046930387013897062106309406874425001127890574986610018093859693455518413268914361859000614904461902442822577552997680098389183082654625098817411306985010658756762152160904278169491634807464356130877526392725432086439934006728914411061861235300979536190100734360684054557448454640750198466877185875290011114667186730452681943043971812380628117527172389889545776779555664826488520325234792648448625225364535053605515386730925070072896004645416713682004600636574389040662827182696337187610904694029221880801372864040345567230941110986028568372710970460116491983700312243090679537497139499778923997433720159174153'
k = 100000

def superDigit(n: str, k):
    full_number = 0

    for digit in n:
        full_number+=int(digit)
    
    full_number = str(full_number*k)
    
    while len(full_number) != 1:
        new_number = 0
        for digit in full_number:
            new_number += int(digit)
        full_number = str(new_number)
    
    return int(full_number)

print(superDigit(n, k))
"""

"""

"""

q_1 = [2, 1, 5, 3, 4]
q_2 = [1, 2, 5, 3, 7, 8, 6, 4]


def minimumBribes(q: list):
    bribes = 0
    for i in range(len(q)):
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        # Count how many people with higher numbers are in front of q[i]
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                bribes += 1
    print(bribes)


minimumBribes(q_1)
minimumBribes(q_2)
