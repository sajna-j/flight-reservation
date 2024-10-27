
-- Create the Flights table
CREATE TABLE Flights (
    id INT PRIMARY KEY AUTO_INCREMENT,
    flight_number VARCHAR(10) NOT NULL,
    departure VARCHAR(100) NOT NULL,
    arrival VARCHAR(100) NOT NULL,
    flight_date DATE NOT NULL
);

-- Create the Users table (if you want to manage users directly)
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL -- Store hashed passwords
);

-- Create the Bookings table
CREATE TABLE Bookings (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    flight_id INT,
    seat_number VARCHAR(5) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES Flights(id) ON DELETE CASCADE
);
