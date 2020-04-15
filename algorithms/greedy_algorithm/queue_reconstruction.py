def reconstruct_queue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    if not (people and len(people) and len(people[0])):
        return [[]]
    people = sorted(people,)

if __name__ == '__main__':
    print(reconstruct_queue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]