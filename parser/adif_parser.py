import adif
import datetime

class ADIFParser:
    """Parses ADIF files and returns structured data."""

    @staticmethod
    def parse(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            log_data = adif.read_from_string(file.read())

        qsos = []
        for record in log_data:
            qsos.append({
                "callsign": record.get("call", ""),
                "qso_date": datetime.datetime.strptime(record.get("qso_date", ""), "%Y%m%d").date(),
                "time_on": record.get("time_on", "00:00:00"),
                "band": record.get("band", ""),
                "freq": float(record.get("freq", 0.0)),
                "mode": record.get("mode", ""),
                "rst_sent": record.get("rst_sent", ""),
                "rst_rcvd": record.get("rst_rcvd", ""),
                "qsl_sent": record.get("qsl_sent", "N") == "Y",
                "qsl_rcvd": record.get("qsl_rcvd", "N") == "Y",
                "grid_square": record.get("gridsquare", ""),
                "country": record.get("country", ""),
                "operator_callsign": record.get("operator", ""),
                "station_callsign": record.get("station_callsign", ""),
                "comment": record.get("comment", "")
            })
        return qsos
