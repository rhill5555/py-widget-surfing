from mysql.connector import MySQLConnection


class SqlComm:
    @staticmethod
    def append_to_table(mysql_connection: MySQLConnection, table: str, columns: str, fields: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""INSERT INTO {table} ({columns}) VALUES ({fields});""")
        #mycursor.execute(f"""INSERT INTO wsl.bios (first_name, last_name, stance, rep_country, home_city, birthday, height, weight, first_season, first_tour) VALUES ('H', 'G', 'R', 'USA', 1, '1989-10-25', 100, 120, '2021', 'test');""")
        mysql_connection.commit()

    def sel_dist_col(mysql_connection: MySQLConnection, table: str, column: str, col_filter: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""SELECT {column} FROM {table} {col_filter}""")
        result = mycursor.fetchall()

        field_lst = []
        for x in result:
            field_lst.append(x)

        print(field_lst[0][0])
        return field_lst

class Places:
    @staticmethod
    def continent(mysql_connection: MySQLConnection):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select continent from wsl.continents")
        result = mycursor.fetchall()

        cont_lst = []
        for x in result:
            cont_lst.append(x[0])

        return sorted(cont_lst, key=str.lower)

    @staticmethod
    def rep_countries(mysql_connection: MySQLConnection):
        mycursor = mysql_connection.cursor()
        mycursor.execute("select country from wsl.countries")
        result = mycursor.fetchall()

        country_lst = []
        for x in result:
            country_lst.append(x[0])

        return sorted(country_lst, key=str.lower)

    @staticmethod
    def countries(mysql_connection: MySQLConnection, continent: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select country.country
                         from wsl.countries country
                         join wsl.continents cont
                              on country.continent_id = cont.id
                         where cont.continent = '{continent}'""")
        result = mycursor.fetchall()

        country_lst = []
        for x in result:
            country_lst.append(x[0])

        return sorted(country_lst, key=str.lower)

    @staticmethod
    def region(mysql_connection: MySQLConnection, country: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select region.region
                         from wsl.regions region
                         join wsl.countries country
                              on region.country_id = country.id
                         where country.country = '{country}'""")
        result = mycursor.fetchall()

        region_lst = []
        for x in result:
            region_lst.append(x[0])

        return sorted(region_lst, key=str.lower)

    @staticmethod
    def city(mysql_connection: MySQLConnection, region: str):
        mycursor = mysql_connection.cursor()
        mycursor.execute(f"""select city.city
                         from wsl.cities city
                         join wsl.regions region
                              on city.region_id = region.id
                         where region.region = '{region}'""")
        result = mycursor.fetchall()

        city_lst = []
        for x in result:
            city_lst.append(x[0])

        return sorted(city_lst, key=str.lower)

    @staticmethod
    def surf_break(mysql_connection: MySQLConnection, city: str):
        pass