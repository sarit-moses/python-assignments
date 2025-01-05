This program analyzes DNA sequences in Fasta or GeneBank format. It currently offers two types of analysis:

Finding the longest sub-sequence that repeats itself at least twice.
Calculating the GC content (percentage of G and C nucleotides).
Usage:

python analyze.py FILE --duplicate --blabla

- FILE: Path to the sequence file.
- --duplicate: (Optional) Find the longest repeat sequence.
- --gc_content: (Optional) Calculate the GC content.
Note: You can run only one or both analyses at the same time by using the corresponding flags.

Example:

python analyze.py my_sequence.fasta --duplicate
This will print the longest repeat sequence and its length for the sequence in my_sequence.fasta.

Requirements:

This program requires the Biopython library. You can install it using pip:

pip install biopython