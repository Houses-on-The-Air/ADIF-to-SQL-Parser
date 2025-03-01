import sys
from parser.adif_parser import ADIFParser
from database.db_factory import DatabaseFactory

def main():
    """
    Main function to parse an ADIF file and insert QSOs into the database.

    This function expects a single command-line argument specifying the path to the ADIF file.
    It parses the ADIF file to extract QSOs and inserts them into the database.

    Usage:
        python main.py <path_to_adif_file>

    If the required command-line argument is not provided, the function prints a usage message
    and exits with a status code of 1.

    The function performs the following steps:
    1. Checks if the command-line argument is provided.
    2. Parses the ADIF file specified by the command-line argument.
    3. Inserts the parsed QSOs into the database.
    4. Closes the database connection.
    5. Prints a success message indicating the number of QSOs imported.

    Raises:
        SystemExit: If the required command-line argument is not provided.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_adif_file>")
        sys.exit(1)

    adif_file = sys.argv[1]
    qsos = ADIFParser.parse(adif_file)

    db = DatabaseFactory.get_database()
    for qso in qsos:
        db.insert_qso(qso)

    db.close()
    print(f"Imported {len(qsos)} QSOs successfully.")

if __name__ == "__main__":
    main()
