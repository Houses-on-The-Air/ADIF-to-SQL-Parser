CREATE DATABASE adif_logs;
GO
USE adif_logs;
GO

-- Table for storing station details
CREATE TABLE stations (
    id INT IDENTITY(1,1) PRIMARY KEY,
    callsign NVARCHAR(20) NOT NULL UNIQUE,
    grid_square NVARCHAR(10),
    cq_zone SMALLINT,
    itu_zone SMALLINT,
    state NVARCHAR(50),
    country NVARCHAR(100)
);
GO

-- Table for storing operator details
CREATE TABLE operators (
    id INT IDENTITY(1,1) PRIMARY KEY,
    callsign NVARCHAR(20) NOT NULL UNIQUE,
    name NVARCHAR(100),
    email NVARCHAR(100)
);
GO

-- Table for storing QSO logs
CREATE TABLE qsos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    station_id INT NOT NULL,
    operator_id INT NOT NULL,
    qso_date DATE NOT NULL,
    time_on TIME NOT NULL,
    time_off TIME NULL,
    callsign NVARCHAR(20) NOT NULL,
    band NVARCHAR(10),
    freq DECIMAL(10,5),
    mode NVARCHAR(10),
    submode NVARCHAR(10),
    rst_sent NVARCHAR(5),
    rst_rcvd NVARCHAR(5),
    qsl_sent BIT DEFAULT 0,
    qsl_rcvd BIT DEFAULT 0,
    qsl_method NVARCHAR(10) CHECK (qsl_method IN ('None', 'Paper', 'LoTW', 'eQSL')) DEFAULT 'None',
    grid_square NVARCHAR(10),
    country NVARCHAR(100),
    comment NVARCHAR(MAX),
    CONSTRAINT fk_qsos_station FOREIGN KEY (station_id) REFERENCES stations(id) ON DELETE CASCADE,
    CONSTRAINT fk_qsos_operator FOREIGN KEY (operator_id) REFERENCES operators(id) ON DELETE CASCADE
);
GO

-- Indexes for faster lookup
CREATE INDEX idx_qso_callsign ON qsos (callsign);
CREATE INDEX idx_qso_date ON qsos (qso_date);
CREATE INDEX idx_station_callsign ON stations (callsign);
CREATE INDEX idx_operator_callsign ON operators (callsign);
GO
