def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)  # best solution


    # son2 = son_years_old * 2
    # if dad_years_old > son2:
    #     return dad_years_old - son2
    # elif dad_years_old < son2:
    #     return son2 - dad_years_old
    # else:
    #     return 0

dad = 6
son = 3
print(twice_as_old(dad, son))