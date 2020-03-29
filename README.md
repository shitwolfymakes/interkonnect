# interkonnect
My RowdyHacks 2020 project

interkonnect is a package allows you to communicate with a piece of software in via SMS.

`demo/demo_movies.py` demonstrates usage.

NOTE: T-Mobile blocks the responses because of their anti-spam, this will not work if you have T-Mobile.

NOTE: before running the demo you will have to create a new Gmail account. 
DO NOT USE an account with anything you care about in it

Store the credentials in a file named `ik_properties.json`, in the same folder as this readme. 
The file should have this structure:
```json
{
    "email" : "<your_email>",
    "pass" : "<your_password>",
    "wait_time" : 2
}
```
This file is in the gitignore so it won't get pushed.

###Demoing
To test the demo, text one of the following command to the Gmail address stored in `ik_properties.json`

Commands:
```
help
list dvd
list bluray
```