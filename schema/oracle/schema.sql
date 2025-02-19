CREATE USER adif_logs IDENTIFIED BY your_password;
GRANT CONNECT, RESOURCE TO adif_logs;
ALTER USER adif_logs QUOTA UNLIMITED ON USERS;

-- Switch to the new schema
ALTER SESSION SET CURRENT_SCHEMA = adif_logs;

-- Table for storing station details
CREATE TABLE stations (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    callsign VARCHAR2(20) NOT NULL UNIQUE,
    grid_square VARCHAR2(10),
    cq_zone NUMBER(2),
    itu_zone NUMBER(2),
    state VARCHAR2(50),
    country VARCHAR2(100)
);

-- Table for storing operator details
CREATE TABLE operators (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    callsign VARCHAR2(20) NOT NULL UNIQUE,
    name VARCHAR2(100),
    email VARCHAR2(100)
);

-- Table for storing QSO logs
CREATE TABLE qsos (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    station_id NUMBER NOT NULL,
    operator_id NUMBER NOT NULL,
    qso_date DATE NOT NULL,
    time_on TIMESTAMP NOT NULL,
    time_off TIMESTAMP,
    callsign VARCHAR2(20) NOT NULL,
    band VARCHAR2(10),
    freq NUMBER(10,5),
    mode VARCHAR2(10),
    submode VARCHAR2(10),
    rst_sent VARCHAR2(5),
    rst_rcvd VARCHAR2(5),
    qsl_sent CHAR(1) DEFAULT 'N' CHECK (qsl_sent IN ('Y', 'N')),
    qsl_rcvd CHAR(1) DEFAULT 'N' CHECK (qsl_rcvd IN ('Y', 'N')),
    qsl_method VARCHAR2(10) DEFAULT 'None' CHECK (qsl_method IN ('None', 'Paper', 'LoTW', 'eQSL')),
    grid_square VARCHAR2(10),
    country VARCHAR2(100),
    comment CLOB,
    CONSTRAINT fk_qsos_station FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
    CONSTRAINT fk_qsos_operator FOREIGN KEY (operator_id) REFERENCES operators(id) ON DELETE CASCADE
);

-- Indexes for faster lookup
CREATE INDEX idx_qso_callsign ON qsos (callsign);
CREATE INDEX idx_qso_date ON qsos (qso_date);
CREATE INDEX idx_station_callsign ON stations (callsign);
CREATE INDEX idx_operator_callsign ON operators (callsign);
