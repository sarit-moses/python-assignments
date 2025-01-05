import argparse
from Bio import SeqIO


def find_longest_repeat(sequence):
    """
    Finds the longest sub-sequence that repeats itself at least twice in the sequence.

    Args:
        sequence: The DNA sequence as a string.

    Returns:
        A tuple containing the longest repeat sequence and its length,
        or (None, None) if no repeats are found.
    """

    longest_repeat = None
    longest_repeat_len = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            subsequence = sequence[i:j]
            if subsequence in sequence[j:]:
                repeat_len = len(subsequence)
                if repeat_len > longest_repeat_len:
                    longest_repeat = subsequence
                    longest_repeat_len = repeat_len

    return longest_repeat, longest_repeat_len


def gc_content(sequence):
    """
    Calculates the GC content of a DNA sequence.

    Args:
        sequence: The DNA sequence as a string.

    Returns:
        The GC content as a float between 0 and 1.
    """

    gc_count = sequence.count("G") + sequence.count("C")
    return gc_count / len(sequence) if len(sequence) > 0 else 0


def analyze_sequence(file_path, find_repeats=False, gc=False):
    """
    Analyzes a DNA sequence in Fasta or GeneBank format.

    Args:
        file_path: The path to the sequence file.
        find_repeats: Whether to find the longest repeat (default: False).
        gc_content: Whether to calculate the GC content (default: False).

    Prints the results of the analysis to the console.
    """

    with open(file_path, "r") as f:
        for record in SeqIO.parse(f, "fasta"):
            sequence = str(record.seq).upper()

            if find_repeats:
                longest_repeat, repeat_len = find_longest_repeat(sequence)
                if longest_repeat:
                    print(f"Longest repeat: {longest_repeat} ({repeat_len} bp)")
                else:
                    print("No significant repeats found.")

            if gc:
                content = gc_content(sequence)
                print(f"GC content: {content:.2f}")

            else:
                print("no analysis was requested; no computation performed")


def main():
    parser = argparse.ArgumentParser(description="Analyze DNA sequence file")
    parser.add_argument("file_path", type=str, help="Path to the Fasta or GeneBank file")
    parser.add_argument(
        "--duplicate", action="store_true", default=False, help="Find longest repeat"
    )
    parser.add_argument("--gc", action="store_true", default=False, help="Calculate GC content")
    args = parser.parse_args()

    analyze_sequence(args.file_path, args.duplicate, args.gc)


if __name__ == "__main__":
    main()