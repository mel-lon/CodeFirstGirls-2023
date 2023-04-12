# foundation-wk5-lesson13 - Session 20 - API Python DB

## 📚 Session Content

- 🎥[Session Recording](https://us06web.zoom.us/rec/share/uu3jjT9KPm7KaVxksPZCwG8nfuXSk1iPdzAXaE1hyuGptcHdprmAtqC8iAXS-TZl.MfO3l81M9djx4FY5)
- ⬜ [Slides](https://docs.google.com/presentation/d/1bAo8dP4dcFqDbKqy0HiL05ZVLyYHbd-B/edit?usp=sharing&ouid=114579717787931838770&rtpof=true&sd=true)
- ⬜ [Simple API](https://github.com/cfgdegree-spring-2023/simple_api)
- ⬜ [Simple API with db](https://github.com/cfgdegree-spring-2023/simple_api/tree/api-db)
- ⬜ [Hotel booking API with db](https://github.com/cfgdegree-spring-2023/python-db-api-example/tree/complete)



## How to set up and run the project

### Install project dependencies
```bash
pip install flask requests mysql-connector-python
```
### Set up a database
- Set up a database called nano by running the `create_db_script.sql` in your database server.
- update the config.py file with your database credentials 
- use the stored procedure call the filldates stored procedure to populate the saloon_bookings table with some time appointment slots
- CAll `nano`.filldates(20230331, 20231231, 'Peter')
- CAll `nano`.filldates(20230331, 20231231, 'Maddie')
- CAll `nano`.filldates(20230331, 20231231, 'Dominic')
### Run the project
open the terminal at the root of your project and run the following command in the terminal to run the project.
```bash
 flask run
 ```

## Endpoints

| Functionality          | Endpoint                        |
|------------------------|---------------------------------|
| View availability Info | GET /availability/<string:date> |
| Add a Booking          | PUT /booking                    |
