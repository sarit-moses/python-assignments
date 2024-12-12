import argparse
from Bio import Entrez
import os
import datetime

def get_data() :
    """ gets current date and time """
    x = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return x

def log_file_exist(filepath):
    """ checks if log file already exists"""
    try:
        return os.path.getsize(filepath)
    except FileNotFoundError:
        return 0

def get_default_rettype(database):
    rettype_mapping = {
        "pubmed": "abstract",
        "nucleotide": "gb",
        "protein": "fasta",
        "gene": "xml", 
    }
    return rettype_mapping.get(database, "xml")  # Default to XML if no specific mapping found


def ncbi_search_and_download(database, search_term, num_results, out_folder, log_file):
    """
    Searches the NCBI database and downloads the specified number of results.
    each result is saved as a separate file in the folder out_folder.

    Args:
        database: The NCBI database to search (e.g., "pubmed", "protein", "nucleotide").
        search_term: The search term.
        num_results: The number of results to retrieve (default: 10).
        out_folder: The folder where to save the files.

    Returns:
        A list of record IDs from the search results.
    """

    Entrez.email = 'sarit.moses@weizmann.ac.il'

    try:
        handle = Entrez.esearch(db=database, term=search_term, retmax=num_results)
        record = Entrez.read(handle)
        print("record")
        handle.close()

        record_ids = record["IdList"]
        total_items = int(record["Count"]) 

        # Create the output folder if it doesn't exist
        os.makedirs(out_folder, exist_ok=True)
        print("dir")

        if record_ids:
            for record_id in record_ids:
                handle = Entrez.efetch(db=database, id=record_id, rettype="fasta", retmode="text")
                record_data = handle.read()
                handle.close()
                # Save each record to a separate file
                file_path = os.path.join(out_folder, f"{database}_{search_term}_{record_id}.txt")
                with open(file_path, "w") as output_file:
                    output_file.write(record_data)

            # save log data to log file
            print(f"Downloaded {len(record_ids)} records from {database} for term '{search_term}' to {out_folder}.")
            with open(log_file, "a") as log:
                if not log_file_exist(log_file): # file did not exist: write header
                    log.write("date,term,max,total\n")
                log.write(f"{get_data()},{search_term},{num_results},{total_items}\n")

            return record_ids, total_items

        else:
            print(f"No results found for term '{search_term}' in {database}.")
            with open(log_file, "a") as log:
                if not log_file_exist(log_file): # file did not exist: write header
                    log.write("date,term,max,total\n")
                log.write(f"{get_data()},{search_term},{num_results},{0}\n")
            return [], 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return [], 0


def main():
    """
    Parses command-line arguments for NCBI search.
    """
    parser = argparse.ArgumentParser(description="NCBI Search Tool")
    parser.add_argument("--database", type=str, default="nucleotide", help="NCBI database to search (e.g., 'pubmed', 'protein'). Default=nucleotide")
    parser.add_argument("--term", type=str, required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Number of results to download. Default=10")
    parser.add_argument("--oo", type=str, default="./", help="Folder in which the search results will be downloaded to. Default is working directory.")
    parser.add_argument("--log", type=str, default="ncbi_search_log.csv", help="log file to save data about each run of the program. Will be saved in the wd where the program is ran from")
    args = parser.parse_args()

    # Access arguments
    database = args.database
    term = args.term
    number_results = args.number
    out_folder = args.oo
    log_file = args.log

    print(f"Searching {database} database for '{term}'")

    # search, download:
    record_ids, total_results = ncbi_search_and_download(database, term, number_results, out_folder, log_file)

    print(f"Retrieving {len(record_ids)} results out of {total_results} search results")

if __name__ == "__main__":
    main()