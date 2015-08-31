db.createUser( { user: "user",
  pwd: "password",
  roles: [ "readWrite", "dbAdmin" ]
} )

db.getSiblingDB('devdb')
