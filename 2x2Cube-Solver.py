import re

# Test case (See below for encoding sequence)
testData = 'BRYRBOBBGGOWYWRGORWWYYOG'

# Rubiks Cube face encode
#          +---+---+
#          | 16| 17|
#          +---+---+
#          | 18| 19|
#  +---+---+---+---+---+---+---+---+
#  | 0 | 1 | 4 | 5 | 8 | 9 | 12| 13|
#  +---+---+---+---+---+---+---+---+
#  | 2 | 3 | 6 | 7 | 10| 11| 14| 15|
#  +---+---+---+---+---+---+---+---+
#          | 20| 21|
#          +---+---+
#          | 22| 23|
#          +---+---+

# Helper Functions


def F(pos):  # Front Clockwise Quarter Turn
    return(pos[0] + pos[20] + pos[2] + pos[21] +
           pos[6] + pos[4] + pos[7] + pos[5] +
           pos[18] + pos[9] + pos[19] + pos[11] +
           pos[12] + pos[13] + pos[14] + pos[15] +
           pos[16] + pos[17] + pos[3] + pos[1] +
           pos[10] + pos[8] + pos[22] + pos[23])


def Fc(pos):  # Front Counterclockwise Quarter Turn
    return (pos[0] + pos[19] + pos[2] + pos[18] +
            pos[5] + pos[7] + pos[4] + pos[6] +
            pos[21] + pos[9] + pos[20] + pos[11] +
            pos[12] + pos[13] + pos[14] + pos[15] +
            pos[16] + pos[17] + pos[8] + pos[10] +
            pos[1] + pos[3] + pos[22] + pos[23])


def U(pos):  # Up Clockwise Quarter Turn
    return (pos[4] + pos[5] + pos[2] + pos[3] +
            pos[8] + pos[9] + pos[6] + pos[7] +
            pos[12] + pos[13] + pos[10] + pos[11] +
            pos[0] + pos[1] + pos[14] + pos[15] +
            pos[18] + pos[16] + pos[19] + pos[17] +
            pos[20] + pos[21] + pos[22] + pos[23])


def Uc(pos):  # Up Counterclockwise Quarter Turn
    return (pos[12] + pos[13] + pos[2] + pos[3] +
            pos[0] + pos[1] + pos[6] + pos[7] +
            pos[4] + pos[5] + pos[10] + pos[11] +
            pos[8] + pos[9] + pos[14] + pos[15] +
            pos[17] + pos[19] + pos[16] + pos[18] +
            pos[20] + pos[21] + pos[22] + pos[23])


def R(pos):  # Right Clockwise Quarter Turn
    return (pos[0] + pos[1] + pos[2] + pos[3] +
            pos[4] + pos[21] + pos[6] + pos[23] +
            pos[10] + pos[8] + pos[11] + pos[9] +
            pos[19] + pos[13] + pos[17] + pos[15] +
            pos[16] + pos[5] + pos[18] + pos[7] +
            pos[20] + pos[14] + pos[22] + pos[12])


def Rc(pos):  # Right Counterclockwise Quarter Turn
    return (pos[0] + pos[1] + pos[2] + pos[3] +
            pos[4] + pos[17] + pos[6] + pos[19] +
            pos[9] + pos[11] + pos[8] + pos[10] +
            pos[23] + pos[13] + pos[21] + pos[15] +
            pos[16] + pos[14] + pos[18] + pos[12] +
            pos[20] + pos[5] + pos[22] + pos[7])

# To check if the Neighbour matches a solution of any combination of possible solutions of a Rubik's cube


def check(V):
    # Using regular expressions
    if re.match('(?=.*OOOO)(?=.*GGGG)(?=.*WWWW)(?=.*RRRR)(?=.*BBBB)(?=.*YYYY).*$', V):
        return True
# Constructs a set to calculate all the legal moves


def N_moves(v):
    # Set of moves from predefined functions
    moves = {F, Fc, R, Rc, U, Uc}
    # Returns a new set Neighbours of v for every move
    return{N(v) for N in moves}

# Solution


def solution(problemInstance):
    print("Solving for the entered 2x2 Rubik's cube")
    print("-----------------------------------------")
    # Base case where D_0 = u and D_j=n_moves(D_0)
    D = [{problemInstance}, set(N_moves(problemInstance))]
    while D[-1]:  # While the second element in D isn't empty...
        D.append(set())  # Append another set
        # For the second last set of vertices...
        for V in D[-2]:
            # For every vertex in the second last set of vertices calculate a new set V_j
            for N in N_moves(V):
                # Check if there is a solution then return the distance travelled
                if check(N):
                    return D
                # Otherwise, if the new set of vertexes. V_j calculated in line 75, are not in the second or third last of V in D then...
                elif N not in D[-2] and V not in D[-3]:
                    # Add the unique vertices to the last set of V in D
                    D[-1].add(N)
        print('Currently at Move '+str(len(D) - 1)+' and still solving...')

# Printing the answer to the solution in a readable format


def printSolution(solutionInstance):
    print("-----------------------------------------")
    print('    The cube can be solved in ' +
          str(len(solutionInstance)-1)+' moves.')
    print("-----------------------------------------")


printSolution(solution(testData))
