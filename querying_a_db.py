import sqlite3
with sqlite3.connect("sitemetrics.db") as connection:
    c = connection.cursor()
##### How many people are from California?  
    c.execute("""SELECT name FROM users WHERE state = "CA" """)
    cali = c.fetchall() #14

##### Who has the most page views? How many do they have, and where are they from?
    c.execute("""SELECT * FROM users WHERE page_views = (SELECT MAX(page_views) FROM users)""")
    most_page_views = c.fetchall() #Edison Mcintyre, 19937, ME

##### Who has the least page views? How many do they have and where are they from?
    c.execute("""SELECT * FROM users WHERE page_views = (SELECT MIN(page_views) FROM users)""")
    least_page_views = c.fetchall() #Hattie Ross, 16, MA

##### Who are the most recent visitors to the site?(at least 3)
    c.execute("""SELECT * FROM users ORDER BY last_visit DESC LIMIT 3;""")
                    #orders by last_visit in descending order, limit only takes in the first 3 values
    recent_visitors = c.fetchall() #Otha Ortiz, Selina Hardy, Terrance Allen all on 2014-10-08

##### Who was the first visitor?
    c.execute("""SELECT * FROM users ORDER BY last_visit LIMIT 1;""")
    first_visitor = c.fetchall() # Woodrow Duffy 2013-10-08

##### Who has an email address with the domain 'horse.edu'?
    c.execute("""SELECT name FROM users WHERE email LIKE "%horse.edu%" """)
    horse_email = c.fetchall() #Fern Byers, Valentine Gonzales
                               #but Fern Byers has hornhorse.edu as the domain

    c.execute("""SELECT name FROM users WHERE email LIKE "%@horse.edu%" """)
    horse_email = c.fetchall()  #Valentine Gonzales

##### How many people are from the city Graford?
    c.execute("""SELECT name FROM users WHERE city = "Graford" """)
    graford_residents = c.fetchall() #Nelly Beach, Corinne Patton, Paulina Rankin

##### What are the names of all the cities that start with the letter V, in alphabetical order?
    c.execute("""SELECT DISTINCT city FROM users WHERE substr(city,1,1) = "V" """)
                #SELECT DISTINCT - prevents repeats    #substr takes a string and clips out a substring from it
    v_cities = c.fetchall() #Van, Valley View, Victoria, Vega

##### What are the names and home cities for people searched for the word "drain"?
    c.execute("""SELECT user.name, user.city FROM users JOIN user_searches ON users.id = user_searches.user_id JOIN search_terms WHERE :word = "drain" """)
    drain_users = c.fetchall()
    print(drain_users)

##### How many times was "trousers" a search term?

##### What were the search terms used by visitors who last visited on August 22 2014?

##### What was the most frequently used search term by people from Idaho?

##### What is the name of user 391, and what are his search terms?

