#https://en.wikipedia.org/wiki/Prime_number_theorem
#https://en.wikipedia.org/wiki/List_of_prime_numbers#The_first_1000_prime_numbers
import math
import time


def runSieve(cap) :
    count = 0
    isCandidateArr = [True] * cap
    isCandidateArr[0] = False
    isCandidateArr[1] = False
    for i in range(2, math.ceil(math.sqrt(cap))):
        if isCandidateArr[i] :
            count += 1
            index = i + i
            while(index < cap) :
                isCandidateArr[index] = False
                index += i
    for k in range(math.ceil(math.sqrt(cap)), cap) :
        if isCandidateArr[k] :
            count += 1
    return count


def validateResults(n, cap) :
    switch={
        10 : n == 4, #ten(10^1)
        100 : n == 25, #hundred(10^2)
        1000 : n == 168, #thousand(10^3)
        10000 : n == 1229, #ten-thousand(10^4)
        100000 : n == 9592, #hundred-thousand(10^5)
        1000000 : n == 78498, #million(10^6)
        10000000 : n == 664579, #ten-million(10^7)
        100000000 : n == 5761455, #hundred-million(10^8)
        1000000000 : n == 50847534, #billion(10^9)
        10000000000 : n == 455052511, #ten-billion(10^10)
        100000000000 : n == 4118054813, #hundred-billion(10^11)
        1000000000000 : n == 37607912018, #trillion(10^12)
        10000000000000 : n == 346065536839, #ten-trillion(10^13)
        100000000000000 : n == 3204941750802 #hundred-trillion(10^14)
    }
    return switch.get(cap)


def main():
    max = 1000000
    start = time.time()
    n = runSieve(max)
    print(n)
    print(validateResults(n,max))
    end = time.time()
    print(end - start)


if __name__ == "__main__" :
    main()