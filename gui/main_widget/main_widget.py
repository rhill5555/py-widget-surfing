import datetime
import sys
from src.sql_commands import Places, SqlComm
from typing import Optional, List

import mysql.connector
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QFileDialog, QButtonGroup
from mysql.connector import MySQLConnection

from gui.main_widget.ui_to_py.wsl_analytics_ui import Ui_MainWindow
from gui.common_widget.dialog_widget.simple_lineedit import SimpleLineEdit

########################################################################################################################

# mycursor = mydb.cursor()
# mycursor.execute("select * from wsl.continents")
# myresult = mycursor.fetchall()


########################################################################################################################

class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, sql_host: str, sql_user: str, sql_password: str):
        # Call the constructor for the inherited QWidget class.
        QMainWindow.__init__(self)


        # Sql Connection Info and mysql connection
        self.__sql_host: str = sql_host
        self.__sql_user: str = sql_user
        self.__sql_password: str = sql_password
        self.__mysql_connection: Optional[MySQLConnection] = None

        # Call the setupUi function that adds all the pyqt stuff to this class, that was designed in the designer.
        # This function is inherited from the Ui_Form class.
        self.setupUi(self)

        # Call the connect_slots function to connect all the event-handlers to functions in this class.
        self.connect_slots()

        # Call to setup everything on the gui.
        self.on_startup()

    @property
    def mysql(self) -> MySQLConnection:
        # Connect to MySQL
        if self.__mysql_connection is None:
            self.__mysql_connection = mysql.connector.connect(
                host=self.__sql_host,
                user=self.__sql_user,
                password=self.__sql_password
            )
        return self.__mysql_connection

    def num_check(self, input_num: str):
        try:
            if input_num == '':
                input_num = 0
            int(input_num)
        except:
            print('Invalid Number')

    # This defines the event handlers for everything.
    def connect_slots(self):
        # Slots for Break Tab
        self.BreakContCb.currentIndexChanged.connect(self.slot_break_cont_cb_on_index_change)
        self.BreakCountryCb.currentIndexChanged.connect(self.slot_break_country_cb_on_index_change)
        self.BreakRegionCb.currentIndexChanged.connect(self.slot_break_region_cb_on_index_change)
        self.addlocationbutton.clicked.connect(self.slot_add_location_btn_on_clicked)
        self.BreakSubmit.clicked.connect(self.slot_break_submit_on_clicked)

        # Slots for Bio Tab
        self.BioHContCb.currentIndexChanged.connect(self.slot_bio_cont_cb_index_changed)
        self.BioHCountryCb.currentIndexChanged.connect(self.slot_bio_country_cb_index_changed)
        self.BioHRegCb.currentIndexChanged.connect(self.slot_bio_region_cb_index_changed)
        self.BioAddlocbutton.clicked.connect(self.slot_add_location_btn_on_clicked)
        self.BioSubmitBut.clicked.connect(self.slot_bio_submit_on_clicked)

    # This setups up everything at the first startup.
    def on_startup(self):
        bio_cont_list = [item for item in Places.continent(mysql_connection=self.mysql)]

        # Add Continents to the combobox.
        self.BreakContCb.addItems(
            [item for item in Places.continent(mysql_connection=self.mysql)]
        )
        self.BioCountCb.addItems(
            [item for item in Places.rep_countries(mysql_connection=self.mysql)]
        )
        self.BioHContCb.addItems(
            [''] + bio_cont_list
        )
        self.BioHCountryCb.clear()
        self.BioHCountryCb.addItems([''])
        self.BioHRegCb.addItems([''])
        self.BioHCityCb.addItems([''])

    # Eventhandler for any button that adds a location to the database.
    def slot_add_location_btn_on_clicked(self):
        dialog = SimpleLineEdit(title="Add a location to the database.", mysql_conn=self.mysql)
        if dialog.exec() == QDialog.Accepted:
            # Continent should never be blank since it has a default
            Continent = dialog.Cont_Cb.currentText()

            # Check to See if Country is Blank for Label and LineEdit
            if not dialog.Country_LineEdit.text() == '':
                Country = dialog.Country_LineEdit.text()
                print(Country)
            elif not dialog.Country_Cb.currentText() == '':
                Country = dialog.Country_Cb.currentText()
                print(Country)
            else:
                print('Country was blank, Dummy Bunny!')
                #raise ValueError()


            # Check to See if Region is Blank for Label and LineEdit
            if not dialog.Region_LineEdit.text() == '':
                Region = dialog.Region_LineEdit.text()
                print(Region)
            elif not dialog.Region_Cb.currentText() == '':
                Region = dialog.Region_Cb.currentText()
                print(Region)
            else:
                print('Region was blank, Dummy Bunny!')
                #raise ValueError()

            # Check to see if City is Blank for Label and LineEdit
            if not dialog.City_LineEdit.text() == '':
                City = dialog.City_LineEdit.text()
                print(City)
            else:
                print('City was blank, Dummy Bunny!')
                #raise ValueError()

        # Add Country to Country Table and raise exception if failed
        try:
            if not dialog.Country_LineEdit.text() == '':
                Country = dialog.Country_LineEdit.text()
                print(Country)
                table = 'wsl.countries'
                columns = 'country, continent_id'
                mycursor = self.mysql.cursor()
                mycursor.execute(f"""SELECT id as continent_id from wsl.continents where continent = '{Continent}'""")
                result = mycursor.fetchall()
                continent_id = result[0][0]
                fields = f"'{Country}', {continent_id}"
                print(f"Table:{table} Columns:{columns} Fields:{fields}")
                SqlComm.append_to_table(
                    mysql_connection=self.mysql,
                    table=table,
                    columns=columns,
                    fields=fields
                )
                print('Country Added')  # Logic to add to table
        except Exception:
            print('Could not append data to wsl.countries')

        # Add Region to Region Table and raise exception if failed
        try:
            if not dialog.Region_LineEdit.text() == '':
                Region = dialog.Region_LineEdit.text()
                table = 'wsl.regions'
                columns = 'region, country_id'
                mycursor = self.mysql.cursor()
                mycursor.execute(f"""SELECT id as country_id from wsl.countries where country = '{Country}'""")
                result = mycursor.fetchall()
                country_id = result[0][0]
                fields = f"'{Region}', {country_id}"
                print(f"Table:{table} Columns:{columns} Fields:{fields}")
                SqlComm.append_to_table(mysql_connection=self.mysql,
                      table=table,
                      columns=columns,
                      fields=fields)
                print('Region Added')  # Logic to add to table
        except Exception:
            print('Could not append data to wsl.regions')

        # Add City to City Table and raise exception if failed
        try:
            table = 'wsl.cities'
            columns = 'city, region_id'
            mycursor = self.mysql.cursor()
            mycursor.execute(f"""SELECT id as region_id from wsl.regions where region = '{Region}'""")
            result = mycursor.fetchall()
            region_id = result[0][0]
            fields = f"'{City}', {region_id}"
            print(f"Table:{table} Columns:{columns} Fields:{fields}")
            SqlComm.append_to_table(mysql_connection=self.mysql,
                table=table,
                columns=columns,
                fields=fields)
            print('City Added')  # Logic to add to table
        except:
            print('Could not append data to wsl.cities')

    ####################################################################################################################
    # Event Handlers for Breaks Tab

    # This is the event handler (slot) for the combobox "breakcontcb" changing index.
    def slot_break_cont_cb_on_index_change(self):
        self.BreakCountryCb.clear()
        self.BreakCountryCb.addItems([item for item in Places.countries(mysql_connection=self.mysql, continent=self.BreakContCb.currentText())])

    # This is the event handler (slot) for the combobox "breakcountrycb" changing index.
    def slot_break_country_cb_on_index_change(self):
        self.BreakRegionCb.clear()
        self.BreakRegionCb.addItems([item for item in Places.region(mysql_connection=self.mysql,
                                                                          country=self.BreakCountryCb.currentText())])


    # This is the event handler (slot) for the combobox "breakregioncb" changing index.
    def slot_break_region_cb_on_index_change(self):
        self.BreakCityCb.clear()
        self.BreakCityCb.addItems([item for item in Places.city(mysql_connection=self.mysql,
                                                                       region=self.BreakRegionCb.currentText())])

    # This is the event handler (slot) for the submit button being clicked.
    def slot_break_submit_on_clicked(self):
        def breaktypelst(*args):
            tempbreaklst = []
            if self.BreakBeachBox.isChecked():
                tempbreaklst.append('Beach')
            if self.BreakPointBox.isChecked():
                tempbreaklst.append('Point')
            if self.BreakReefBox.isChecked():
                tempbreaklst.append('Reef')
            if self.BreakRiverBox.isChecked():
                tempbreaklst.append('River')
            if self.BreakEngBox.isChecked():
                tempbreaklst.append('Engineered')
            if self.BreakSandbarBox.isChecked():
                tempbreaklst.append('Sandbar')
            if self.BreakBreakwaterBox.isChecked():
                tempbreaklst.append('Breakwater')
            if self.BreakJettiesBox.isChecked():
                tempbreaklst.append('Jetties')
            return tempbreaklst

        # Check to see if Break is Blank for Label and LineEdit
        if not self.BreakBreakEntry.text() == '':
            Break = self.BreakBreakEntry.text()
            print(Break)
            breakCity = self.BreakCityCb.currentText()
            print(breakCity)
            breaktype = breaktypelst()
            print(breaktype)

            if self.BreakBurnLight.isChecked():
                breakburn = 'Light'
            elif self.BreakBurnMed.isChecked():
                breakburn = 'Medium'
            elif self.BreakBurnEx.isChecked():
                breakburn = 'Exhausting'
            print(breakburn)
        else:
            print('Break was blank, Dummy Bunny!')
            # raise ValueError()

        breaktype_str_1 = ""
        # Add Break to Break Table and raise exception if failed
        try:
            table = 'wsl.breaks'
            columns = 'break, city_id, break_type, sldr_burn'
            mycursor = self.mysql.cursor()
            mycursor.execute(f"""SELECT id as city_id from wsl.cities where city = '{breakCity}'""")
            result = mycursor.fetchall()
            city_id = result[0][0]

            for ind, item in enumerate(breaktype):
                if not ind == (len(breaktype) - 1):
                    breaktype_str_1 = breaktype_str_1 + item + ', '
                else:
                    breaktype_str_1 = breaktype_str_1 + item

            fields = f"'{Break}', {city_id}, '{breaktype_str_1}', '{breakburn}'"
            print(f"Table:{table} Columns:{columns} Fields:{fields}")
            SqlComm.append_to_table(mysql_connection=self.mysql,
                                    table=table,
                                    columns=columns,
                                    fields=fields)
            print('Break Added')  # Logic to add to table
        except:
            print('Could not append data to wsl.breaks')

    ####################################################################################################################
    # Bio Tab

    # Bio Continent Select

    def slot_bio_cont_cb_index_changed(self):
        self.BioHCountryCb.clear()
        self.BioHCountryCb.addItems([item for item in Places.countries(mysql_connection=self.mysql,
                                                                           continent=self.BioHContCb.currentText())])

    def slot_bio_country_cb_index_changed(self):
        self.BioHRegCb.clear()
        self.BioHRegCb.addItems([item for item in Places.region(mysql_connection=self.mysql,
                                                                           country=self.BioHCountryCb.currentText())])

    def slot_bio_region_cb_index_changed(self):
        self.BioHCityCb.clear()
        self.BioHCityCb.addItems([item for item in Places.city(mysql_connection=self.mysql,
                                                                           region=self.BioHRegCb.currentText())])

    # Bio Tab Submit
    def slot_bio_submit_on_clicked(self):
        if not self.BioFirNmeLine.text() == '':
            print('First Name Success')
            if not self.BioLastNmeLine.text() == '':
                print('Last Name Success')

                first_name = self.BioFirNmeLine.text()
                print(first_name)
                last_name = self.BioLastNmeLine.text()
                print(last_name)

                rep_country = self.BioCountCb.currentText()
                print(rep_country)
                first_season = self.BioFirSeasonCb.text()
                print(first_season)
                first_tour = self.BioFirstTourLine.text()
                print(first_tour)

                if not self.BioHCityCb.currentText() == '':
                    home_city = self.BioHCityCb.currentText()
                    table = 'wsl.cities'
                    column = 'id'
                    col_filter = f"where city = '{home_city}'"
                    city_id = SqlComm.sel_dist_col(mysql_connection=self.mysql, table=table, column=column, col_filter=col_filter)
                    city_id = city_id[0][0]
                else:
                    city_id = 500

                try:
                    if self.BioBdayLine.text() == '':
                        birthday = '1900-01-01'
                    else:
                        dt_string = self.BioBdayLine.text()
                        dt_format = '%m/%d/%Y'
                        birthday = datetime.datetime.strptime(dt_string, dt_format)
                        print(birthday)
                except:
                    print(f"Oh No! That day of birth is not on the Gregorian Calendar!" )

                ht = self.BioHtLine.text()
                if ht == '':
                    height = 0
                else:
                    self.num_check(input_num=ht)
                    height = int(ht)
                print(height)

                wt = self.BioWtLine.text()
                if wt == '':
                    weight = 0
                else:
                    self.num_check(input_num=wt)
                    weight = int(wt)
                print(weight)

                if self.BioRegBut.isChecked():
                    Stance = 'R'
                elif self.BioGoofBut.isChecked():
                    Stance = 'G'
                else:
                    Stance = ''
                print(Stance)

                if self.MaleBox.isChecked() and self.FemaleBox.isChecked():
                    print("Choose either Male or Female Tour")
                elif self.MaleBox.isChecked():
                    gender = 'Male'
                elif self.FemaleBox.isChecked():
                    gender = 'Female'
                else:
                    print("Select Male or Female Tour")
                    raise ValueError
                print(gender)

            else:
                print("Last Name is blank, Dummy Bunny!")
        else:
            print("First Name is blank, Dummy Bunny!")

        # Add to Bios Table
        try:
            table = 'wsl.bios'
            columns = 'gender, first_name, last_name, stance, rep_country, home_city, birthday, height, weight, first_season, first_tour'
            fields = f"'{gender}', '{first_name}', '{last_name}', '{Stance}', '{rep_country}', {city_id}, '{birthday}', {height}, {weight}, '{first_season}', '{first_tour}'"
            print(f"Table:{table} Columns:{columns} Fields:{fields}")
            SqlComm.append_to_table(mysql_connection=self.mysql,
                                    table=table,
                                    columns=columns,
                                    fields=fields)
            print('Bio Added')  # Logic to add to table

        except:
            print('Could not append data to wsl.bios')

        self.BioFirNmeLine.clear()
        self.BioLastNmeLine.clear()
        self.BioBdayLine.clear()
        self.BioHtLine.clear()
        self.BioWtLine.clear()
        self.BioFirSeasonCb.clear()
        self.BioFirstTourLine.clear()
        self.MaleBox.setChecked(0)
        self.FemaleBox.setChecked(0)
        self.BioRegBut.setChecked(0)
        self.BioGoofBut.setChecked(0)

########################################################################################################################
if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget(sql_host='localhost', sql_user='Heather', sql_password='#LAwaItly19')
    win.show()

    sys.exit(app.exec())