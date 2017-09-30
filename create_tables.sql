CREATE TABLE User (
	UserID int 				NOT NULL,
	FirstName varchar(255) 	NOT NULL,
	LastName varchar(255)	NOT NULL,
	Password varchar(15)	NOT NULL,
	Email varchar(255)		NOT NULL,

	PRIMARY KEY (UserID)
);

CREATE TABLE Blog(
	UserID int				NOT NULL,
	BlogID int				NOT NULL,
	Title varchar(255)		NOT NULL,
	TimeCreated datetime	NOT NULL,
	Type enum('preparation', 'reflection', 'share'),
	Content text,
	FOREIGN KEY (UserID)
			REFERENCES User(UserID),
	PRIMARY KEY (BlogID)
);

CREATE TABLE Map(
	UserID int				NOT NULL,
	MapID int 				NOT NULL,
	PRIMARY KEY (MapID),
	FOREIGN KEY (UserID)
		REFERENCES User(UserID)
);

CREATE TABLE Journey(
	JourneyID int 			NOT NULL,
	Description varchar(255),
	Lat decimal(6,4)		NOT NULL,
	Lon decimal(6,4)		NOT NULL,
	PRIMARY KEY (JourneyID)
);

CREATE TABLE User_Journeys (
	UserID int 				NOT NULL,
	JourneyID int			NOT NULL,
	FOREIGN KEY (UserID)
		REFERENCES User(UserID)
		ON DELETE CASCADE,
	FOREIGN KEY (JourneyID)
		REFERENCES Journey(JourneyID)
		ON DELETE CASCADE,
	PRIMARY KEY(UserID, JourneyID)

);

CREATE TABLE Map_Journeys (
	MapID int				NOT NULL,
	JourneyID int			NOT NULL,
	FOREIGN KEY (MapID)
		REFERENCES Map(MapID)
		ON DELETE CASCADE,
	FOREIGN KEY (JourneyID)
		REFERENCES Journey(JourneyID)
		ON DELETE CASCADE,
	PRIMARY KEY(MapID, JourneyID)


);
