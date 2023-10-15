CREATE USER 'user1'@'%' IDENTIFIED BY 'password1';
GRANT ALL PRIVILEGES ON mysql.* TO 'user1'@'%' IDENTIFIED BY 'password1' WITH GRANT OPTION;
FLUSH PRIVILEGES;

use mysql;

create table users (
    id int not null auto_increment,
    username varchar(255) not null,
    email varchar(255) not null UNIQUE,
    password varchar(255) not null,
    is_active boolean,
    is_superuser boolean,
    created_at datetime not null,
    updated_at datetime not null,
    primary key (id)
);