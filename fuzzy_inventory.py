import math
import matplotlib.pyplot as plt


seq = []

# write down the number zero
# write down the number if times you just wrote down that number or two less than it
# repeat
def iterate_seq():
    if len(seq) == 0:
        seq.append(0)
        return

    s = seq[-1]
    seq.append(seq.count(s) + seq.count(s - 2)) # chaotic, interesting!!!

    ## subtracting any number >= 2 seems to produce a similar chaos
    ## they all seem to be bound by sqrt(n) (literally just the eyeball test I did not graph sqrt(n) alongside these lol)


    #seq.append(seq.count(s) + seq.count(s - 1)) # behaves orderly, envalope looks like sqrt(n)

    #seq.append(seq.count(s) + seq.count(s + 1)) # very orderly

    #seq.append(seq.count(s) + seq.count(s + 1) + seq.count(s - 1)) ## very orderly

    #seq.append(seq.count(s) + seq.count(s - 1) + seq.count(s - 2)) ## also very chaotic


def main():

    #define the range of terms that will be generated here
    range_ = range(0, 30000) 

    for n in range_:
        iterate_seq()

    plt.scatter(range_, seq, 0.1)

    for i in range(0, 20):
        print(str(seq[i]) + ','),
    plt.show()

    with open("b327296.txt", 'w') as outfile:
        for i in range_:
            outfile.write(str(i) + " " + str(seq[i]) + "\n")
    outfile.close()


if __name__ == "__main__":
    main()


