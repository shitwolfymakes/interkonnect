# interkonnect
My RowdyHacks 2020 project

interkonnect is a package allows you to communicate with a piece of software in via SMS.

`demo/demo_movies.py` demonstrates usage.

NOTE: before running the demo you will have to create a new Gmail account. 
DO NOT USE an account with anything you care about in it

Store the credentials in a file named `ik_properties.json`, that has this structure:
```json
{
    "email" : "",
    "pass" : "",
    "wait_time" : 2
}
```

Commands:
```
help
list dvd
list bluray
```