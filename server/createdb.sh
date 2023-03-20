#brew install postgresql

#brew services start postgresql@12
#brew services stop postgresql

#psql postgres

CREATE ROLE webtutor WITH LOGIN PASSWORD 'test';
ALTER ROLE webtutor CREATEDB;

\q

psql postgres -U webtutor

#createdb webtutor

postgresql://username:password@localhost:5432/testdb