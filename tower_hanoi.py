# Tower of Hanoi Solution
def tower_hanoi(discs, start='A', interm='B', dest='C'):
    if discs == 0:
        return
    else:
        tower_hanoi(discs-1, start, dest, interm)
        print(f"Move {start} to {dest}")
        return tower_hanoi(discs-1, interm, start, dest)


tower_hanoi(3)
