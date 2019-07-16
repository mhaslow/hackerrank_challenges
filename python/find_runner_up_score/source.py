if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list_of_ints = list(set(arr))
    list_of_ints.sort()
    print(list_of_ints[len(list_of_ints) - 2])
