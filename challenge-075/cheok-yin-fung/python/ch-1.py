# Python3
# Perl Weekly Challenge #075 Task 1 Coins Sum, Python script

# coins = [1, 2, 3, 5]
# total = 5
# --> len(arr_for_dp[total]) == 6

# coins = [1, 2, 3, 4, 5]
# total = 5
# --> len(arr_for_dp[total]) == 7

def coins_sum(uinput):
    userinput = list(uinput).copy()
    total = userinput.pop(0)
    coins = userinput
    dp_range = []
    arr_for_dp = [ [] ]

    for i_ in range(total):
        dp_range.append(i_ + 1)


    j = 0
    for i in dp_range:
        if i == coins[j]:
            arr_for_dp.append([ [coins[j]] ])
            if j < len(coins)-1:
                j = j+1 
        else:
            arr_for_dp.append([])

    for i in dp_range:
        for k in range(len(coins)):
            if (i-coins[k] > 0):
                for p in range(len(arr_for_dp[i-coins[k]])):
                    partition = arr_for_dp[i-coins[k]][p]
                    partition_p = list(partition).copy()
                    partition_p.append(coins[k])
                    partition_p = sorted(partition_p)
                    if not(partition_p in arr_for_dp[i]):
                        arr_for_dp[i].append(list(partition_p).copy())

    return arr_for_dp[total]


if __name__ == "__main__":
    target = int(input("Enter the sum: \n"))
    urinput = [target]
    coins_sum_len = int(input("Enter number of varieties of coins:\n")) 
    print("Enter the value of coins with line breaks")
    for i in range(coins_sum_len):
        urinput.append(int(input()))

    ans = coins_sum( urinput )
    print("===================")
    for item in ans:
        print(item)
    print("answer: ", len(ans))
