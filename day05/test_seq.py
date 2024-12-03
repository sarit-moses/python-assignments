from seq import count_stats, main


def test_count_stats():
    filelist = ["a_seq.txt", "b_seq.txt"]
    assert count_stats(filelist[0]) == [2, 5, 7, 6, 7, 27]
    assert count_stats(filelist[1]) == [1, 2, 4, 3, 0, 10]
    assert len(count_stats(filelist[0])) == 6

def test_main():
    filelist = ["a_seq.txt", "b_seq.txt"]
    assert main(filelist) == [3, 7, 11, 9, 7, 37]

