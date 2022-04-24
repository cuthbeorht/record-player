# Simple Todo App

This is a simple todo app

## Database

Setup user SQL:

```sql
create database todo;

create user todo with encrypted password 'odot';

grant all privileges on database todo to todo;
```