CREATE DATABASE IF NOT EXISTS adif_logs;
USE adif_logs;

-- Table for storing station details
CREATE TABLE stations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    callsign VARCHAR(20) NOT NULL,
    grid_square VARCHAR(10),
    cq_zone INT,
    itu_zone INT,
    state VARCHAR(50),
    country VARCHAR(100),
    UNIQUE(callsign)
);

-- Table for storing operator details
CREATE TABLE operators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    callsign VARCHAR(20) NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100),
    UNIQUE(callsign)
);

-- Table for storing QSO logs
CREATE TABLE qsos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    station_id INT NOT NULL,
    operator_id INT NOT NULL,
    qso_date DATE NOT NULL,
    time_on TIME NOT NULL,
    time_off TIME,
    callsign VARCHAR(20) NOT NULL,
    band VARCHAR(10),
    freq DECIMAL(10,5),
    mode VARCHAR(10),
    submode VARCHAR(10),
    rst_sent VARCHAR(5),
    rst_rcvd VARCHAR(5),
    qsl_sent BOOLEAN DEFAULT FALSE,
    qsl_rcvd BOOLEAN DEFAULT FALSE,
    qsl_method ENUM('None', 'Paper', 'LoTW', 'eQSL') DEFAULT 'None',
    grid_square VARCHAR(10),
    country VARCHAR(100),
    address VARCHAR(255)
    comment TEXT,
    FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
    FOREIGN KEY (operator_id) REFERENCES operators(id) ON DELETE CASCADE
);

-- Indexes for faster lookup
CREATE INDEX idx_qso_callsign ON qsos (callsign);
CREATE INDEX idx_qso_date ON qsos (qso_date);
CREATE INDEX idx_station_callsign ON stations (callsign);
CREATE INDEX idx_operator_callsign ON operators (callsign);
