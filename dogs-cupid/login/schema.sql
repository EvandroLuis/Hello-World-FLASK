drop table if exists entries;

create table owner (
  id integer primary key autoincrement,
  name text not null,
  email text not null,
  password text not null,
  telephone integer not null,
  country text not null,
  city text
  );
