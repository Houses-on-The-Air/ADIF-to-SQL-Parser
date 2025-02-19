import sys
from parsers.adif_parser import ADIFParser
from db_factory import DatabaseFactory

def main():
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
