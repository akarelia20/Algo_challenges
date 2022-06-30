As a backend enginner you were tasked to devlope a fast in memory datastructure to manage user profile information (username, name, email) for 100 million users. it should allowe following:

- Insert in profile info for new user
- Find the profile info for a user given their username
- update the profile info for a user of the platform given their username
- list all the users in the platform sorted by their username.

Assue all the usernames are unique

# thought process/psudocode

- firstly define user class and crerated some users
- then difine databse class
- in database class constuctor create a uselist which is empty at start.
- define a method in the database class which adds a user by itrating through userlist.
- and if current.user.name is > user.name that place the user at the current itratinfg position.
