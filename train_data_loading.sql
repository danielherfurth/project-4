

-- Loading the train dataset into SQL table

CREATE TABLE train_data
 
(

  id VARCHAR (30) PRIMARY KEY,

  title VARCHAR (max), 

  author VARCHAR(max),

  text VARCHAR(max),

  label VARCHAR(max)
	
);