for i in range(1,11):
    for j in range(1,11):
        if (i*j) <= 9:
            print(f"  {i*j}", end='\t')
        elif(i*j) < 100:
            print(f" {i*j}", end='\t')
        else:
            print(format(i*j), end='\t')
    print('\n')