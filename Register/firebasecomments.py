from firebase import firebase

firebase = firebas("he.FirebaseApplicationttps://comments-3edb1-default-rtdb.firebaseio.com/",None)
data = [{
    "name": "Arvie",
    "email": "arvie@gmail.com",
    "message": "Hi, there folks, welcome to Vision Labs. Post your projects here.",
    "timestamp": "11/01/2021"
  },
  {
    "name": "Rohan",
    "email": "rohan@gmail.com",
    "message": "I will post my projects here.",
    "timestamp": "12/01/2021"
  },
  {
    "name": "Sijo",
    "email": "arvie@gmail.com",
    "message": "I like this project.",
    "timestamp": "13/01/2021"
  }
  ]

for i in data:
    result = firebase.post('comments-3edb1-default-rtdb/Customer',i)
    print(data)