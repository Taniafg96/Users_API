CREATE USER 'user1'@localhost IDENTIFIED BY 'password1';
GRANT ALL PRIVILEGES ON *.* TO 'user1'@localhost IDENTIFIED BY 'password1';
FLUSH PRIVILEGES;

use mysql;

create table users (
    id int not null auto_increment,
    username varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    is_active boolean,
    is_superuser boolean,
    created_at datetime not null,
    updated_at datetime not null,
    primary key (id)
);