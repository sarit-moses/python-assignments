###############
### imports ###
###############

import sys

#################
### functions ###
#################

def count_stats(filepath):
    """
    input: filepath (string)
    output: number of appearances of each nucleotide in the file. non-nucleotide characters will be considered unknown
    """
    with open(filepath, "r") as f:
        seq = f.read()[:-1]
        A = seq.count("A") + seq.count("a")
        C = seq.count("C") + seq.count("c")
        T = seq.count("T") + seq.count("t")
        G = seq.count("G") + seq.count("g")
        Total = len(seq)
        Unknown = Total - (A + C + T + G)
    return [A, C, T, G, Unknown, Total]

def print_stats(stats):
    """ 
    input: list of integers with length 6 of stats: A, C, T, G, Unknown, Total
    output: prints stats
    return: None
    """
    print(f"A:\t\t{stats[0]}\t{round((stats[0]/stats[5])*100, 1)}%")
    print(f"C:\t\t{stats[1]}\t{round((stats[1]/stats[5])*100, 1)}%")
    print(f"T:\t\t{stats[2]}\t{round((stats[2]/stats[5])*100, 1)}%")
    print(f"G:\t\t{stats[3]}\t{round((stats[3]/stats[5])*100, 1)}%")
    print(f"Unknown:\t{stats[4]}\t{round((stats[4]/stats[5])*100, 1)}%")
    print(f"Total:\t{stats[5]}")
    print()

def main(filenames):
    combo_stats = [0 for i in range(6)]
    for filepath in filenames:
        stats = count_stats(filepath) # get stats for single file
        for i in range(6):
            combo_stats[i] += stats[i] # add stats to total in all files
        # print stats for single file
        print(filepath)
        print_stats(stats)
    # print stats of all files combined
    print("All")
    print_stats(combo_stats)
    return combo_stats

###########
### run ###
###########

if __name__ == "__main__" :
    args = sys.argv[1:]
    main(args)
    
