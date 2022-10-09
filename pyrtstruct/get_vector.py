
def get_vector(vect):
    vect = vect.split()
    vector = []
    for select in range(len(vect)):
        try:
            vector.append(int(vect[select]))
        except ValueError:
            print('Chars neglected')
    return vector
