### READ ###
READ_USERS = """ SELECT * FROM users; """
READ_ONE_USER = """ SELECT * FROM users WHERE id = {}; """

### CREATE ###
CREATE_USER = """ INSERT INTO 
users (username, email, password, is_active, is_superuser, created_at, updated_at) 
VALUES ('{}', '{}', '{}', {}, {}, '{}', '{}'); """

### UPDATE ###
UPDATE_USER = """ UPDATE users SET {} WHERE id = {}; """

### DELETE ###
DELETE_USER = """ DELETE FROM users WHERE id = {}; """