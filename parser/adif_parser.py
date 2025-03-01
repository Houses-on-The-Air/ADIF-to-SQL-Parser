import re
import datetime

class ADIFParser:
    """
    Parses ADIF files and returns structured QSO data.

    Methods:
        parse(file_path):

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file content cannot be parsed correctly.
        KeyError: If required fields are missing in the QSO record.
    """

    @staticmethod
    def parse(file_path):
        """
        Parses an ADIF (Amateur Data Interchange Format) file and extracts QSO (contact) records.

        Args:
            file_path (str): The path to the ADIF file to be parsed.

        Returns:
            list: A list of dictionaries, each representing a QSO record with the following keys:
                - callsign (str): The callsign of the contacted station.
                - qso_date (datetime.date): The date of the QSO.
                - time_on (str): The time the QSO started.
                - band (str): The band on which the QSO was made.
                - freq (float or None): The frequency of the QSO.
                - mode (str): The mode of the QSO (e.g., CW, SSB).
                - rst_sent (str): The signal report sent.
                - rst_rcvd (str): The signal report received.
                - qsl_sent (bool): Whether a QSL card was sent.
                - qsl_rcvd (bool): Whether a QSL card was received.
                - grid_square (str): The grid square of the contacted station.
                - country (str): The country of the contacted station.
                - operator_callsign (str): The callsign of the operator.
                - station_callsign (str): The callsign of the station.
                - comment (str): Any additional comments.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        qsos = []
        qso_data = content.split("<eor>")  # Split by end-of-record

        for qso in qso_data:
            qso_dict = {}

            # Extract fields like <CALL:6>W1AW
            matches = re.findall(r"<(.*?):(\d+)>([^<]+)", qso)

            for field, _, value in matches:
                qso_dict[field.lower()] = value.strip()

            if "call" in qso_dict and "qso_date" in qso_dict:
                qsos.append({
                    "callsign": qso_dict.get("call", ""),
                    "qso_date": datetime.datetime.strptime(qso_dict.get("qso_date", ""), "%Y%m%d").date(),
                    "time_on": qso_dict.get("time_on", "00:00:00"),
                    "band": qso_dict.get("band", ""),
                    "freq": float(qso_dict.get("freq", 0.0)) if "freq" in qso_dict else None,
                    "mode": qso_dict.get("mode", ""),
                    "rst_sent": qso_dict.get("rst_sent", ""),
                    "rst_rcvd": qso_dict.get("rst_rcvd", ""),
                    "qsl_sent": qso_dict.get("qsl_sent", "N") == "Y",
                    "qsl_rcvd": qso_dict.get("qsl_rcvd", "N") == "Y",
                    "grid_square": qso_dict.get("gridsquare", ""),
                    "country": qso_dict.get("country", ""),
                    "operator_callsign": qso_dict.get("operator", ""),
                    "station_callsign": qso_dict.get("station_callsign", ""),
                    "comment": qso_dict.get("comment", "")
                })

        return qsos
