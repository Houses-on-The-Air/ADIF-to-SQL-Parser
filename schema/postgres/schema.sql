CREATE DATABASE adif_logs;
\c adif_logs;

-- Table for storing station details
CREATE TABLE stations (
    id SERIAL PRIMARY KEY,
    callsign VARCHAR(20) NOT NULL UNIQUE,
    grid_square VARCHAR(10),
    cq_zone SMALLINT,
    itu_zone SMALLINT,
    state VARCHAR(50),
    country VARCHAR(100)
);

-- Table for storing operator details
CREATE TABLE operators (
    id SERIAL PRIMARY KEY,
    callsign VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Table for storing QSO logs
CREATE TABLE qsos (
    id SERIAL PRIMARY KEY,
    station_id INT NOT NULL,
    operator_id INT NOT NULL,
    qso_date DATE NOT NULL,
    time_on TIME NOT NULL,
    time_off TIME,
    callsign VARCHAR(20) NOT NULL,
    band VARCHAR(10),
    freq NUMERIC(10,5),
    mode VARCHAR(10),
    submode VARCHAR(10),
    rst_sent VARCHAR(5),
    rst_rcvd VARCHAR(5),
    qsl_sent BOOLEAN DEFAULT FALSE,
    qsl_rcvd BOOLEAN DEFAULT FALSE,
    qsl_method TEXT CHECK (qsl_method IN ('None', 'Paper', 'LoTW', 'eQSL')),
    grid_square VARCHAR(10),
    country VARCHAR(100),
    comment TEXT,
    CONSTRAINT fk_qsos_station FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
    CONSTRAINT fk_qsos_operator FOREIGN KEY (operator_id) REFERENCES operators(id) ON DELETE CASCADE
);

-- Indexes for faster lookup
CREATE INDEX idx_qso_callsign ON qsos (callsign);
CREATE INDEX idx_qso_date ON qsos (qso_date);
CREATE INDEX idx_station_callsign ON stations (callsign);
CREATE INDEX idx_operator_callsign ON operators (callsign);
