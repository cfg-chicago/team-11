CREATE TABLE User (
	UserID int AUTO_INCREMENT PRIMARY KEY,
	FirstName varchar(255) NOT NULL,
	LastName varchar(255) NOT NULL,
	Password varchar(15) NOT NULL,
	Email varchar(255) NOT NULL

);

CREATE TABLE Blog(
	UserID int NOT NULL,
	BlogID int AUTO_INCREMENT PRIMARY KEY,
	Created timestamp DEFAULT now(),
	Type enum('preparation', 'reflection', 'share'),
	Content text
);

CREATE TABLE Map(
	UserID int NOT NULL,
	MapID int AUTO_INCREMENT PRIMARY KEY,
	FOREIGN KEY (UserID)
		REFERENCES User(UserID)
);

CREATE TABLE Journey(
	JourneyID int AUTO_INCREMENT PRIMARY KEY,
	Description varchar(255),
	Lat decimal(6,4) NOT NULL,
	Lon decimal(6,4) NOT NULL
);

CREATE TABLE User_Journeys (
	UserID int NOT NULL,
	JourneyID int NOT NULL,
	FOREIGN KEY (UserID)
		REFERENCES User(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY (JourneyID)
		REFERENCES Journey(JourneyID)
		ON DELETE CASCADE,
	PRIMARY KEY(UserID, JourneyID)

);

CREATE TABLE Journey_Blogs (
	JourneyID int NOT NULL,
	BlogID int NOT NULL,
	FOREIGN KEY (JourneyID)
		REFERENCES Journey(JourneyID)
		ON DELETE CASCADE,
	FOREIGN KEY (BlogID)
		REFERENCES Blog(BlogID)
		ON DELETE CASCADE,
	PRIMARY KEY(JourneyID, BlogID)
);

CREATE TABLE Map_Journeys (
	MapID int NOT NULL,
	JourneyID int NOT NULL,
	FOREIGN KEY (MapID)
		REFERENCES Map(MapID)
		ON DELETE CASCADE,
	FOREIGN KEY (JourneyID)
		REFERENCES Journey(JourneyID)
		ON DELETE CASCADE,
	PRIMARY KEY(MapID, JourneyID)


);
