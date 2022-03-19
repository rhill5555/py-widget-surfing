import datetime
import sys
from src.sql_commands import Places, SqlComm
from typing import Optional, List

import mysql.connector
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog, QFileDialog
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
        # Add Continents to the combobox.
        self.BreakContCb.addItems(
            [item[0] for item in Places.continent(mysql_connection=self.mysql)]
        )
        self.BioCountCb.addItems(
            [item[0] for item in Places.rep_countries(mysql_connection=self.mysql)]
        )
        self.BioFirSeasonCb.addItems(
            [item for item in ['2022', '2021', '2020', '2019']]
        )
        self.BioHContCb.addItems(
            [item[0] for item in Places.continent(mysql_connection=self.mysql)]
        )
        self.BioHCountryCb.clear()

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
        self.BreakCountryCb.addItems([item[0] for item in Places.countries(mysql_connection=self.mysql, continent=self.BreakContCb.currentText())])

    # This is the event handler (slot) for the combobox "breakcountrycb" changing index.
    def slot_break_country_cb_on_index_change(self):
        self.BreakRegionCb.clear()
        self.BreakRegionCb.addItems([item[0] for item in Places.region(mysql_connection=self.mysql,
                                                                          country=self.BreakCountryCb.currentText())])


    # This is the event handler (slot) for the combobox "breakregioncb" changing index.
    def slot_break_region_cb_on_index_change(self):
        self.BreakCityCb.clear()
        self.BreakCityCb.addItems([item[0] for item in Places.city(mysql_connection=self.mysql,
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
        self.BioHCountryCb.addItems([item[0] for item in Places.countries(mysql_connection=self.mysql,
                                                                           continent=self.BioHContCb.currentText())])

    def slot_bio_country_cb_index_changed(self):
        self.BioHRegCb.clear()
        self.BioHRegCb.addItems([item[0] for item in Places.region(mysql_connection=self.mysql,
                                                                           country=self.BioHCountryCb.currentText())])

    def slot_bio_region_cb_index_changed(self):
        self.BioHCityCb.clear()
        self.BioHCityCb.addItems([item[0] for item in Places.city(mysql_connection=self.mysql,
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
                first_season = self.BioFirSeasonCb.currentText()
                print(first_season)
                first_tour = self.BioFirTourCb.currentText()
                print(first_tour)

                home_city = self.BioHCityCb.currentText()
                print(home_city)
                table = 'wsl.continents'
                column = 'continent'
                SqlComm.sel_dist_col(mysql_connection=self.mysql, table=table, column=column)


                try:
                    if self.BioBdayLine.text() == '':
                        birthday = '01/01/1900'
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

            else:
                print("Last Name is blank, Dummy Bunny!")
        else:
            print("First Name is blank, Dummy Bunny!")



########################################################################################################################
if __name__ == '__main__':
    app = QApplication([])
    win = MainWidget(sql_host='localhost', sql_user='Heather', sql_password='#LAwaItly19')
    win.show()

    sys.exit(app.exec())