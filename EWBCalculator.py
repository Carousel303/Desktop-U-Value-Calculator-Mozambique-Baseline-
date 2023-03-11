from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from EWB_Calculator_2 import Ui_Dialog

# floor options
dense_cast_concrete = 1.4
light_cast_concrete = 0.4
hardwood = 0.16
oil_palm_fiber = 0.073

# wall options
dense_cast_concrete = 1.4
light_cast_concrete = 0.4
compacted_earth_brick = 0.625
reeds = 0.051
bagasse = 0.051
cotton_stalks = 0.07
date_palm = 0.0785
pineapple_leaves = 0.0385
oil_palm_fiber = 0.073
straw_bale = 0.0525

# window options
glass = 0.8

# roof options
dense_cast_concrete = 1.4
light_cast_concrete = 0.4
straw = 0.06
bamboo = 0.5
reeds = 0.051
bagasse = 0.051
cotton_stalks = 0.07
date_palm = 0.0785
pineapple_leaves = 0.0385
oil_palm_fiber = 0.073


class EWBCalculator(qtw.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Add the following line to create a reference to the label in the UI
        self.lblCalculationResult = self.ui.lblCalculationResult

        # add materials to dropdown material menus
        # floor materials
        self.ui.comboBox_5.addItem("Dense Cast Concrete")
        self.ui.comboBox_5.addItem("Light Cast Concrete")
        self.ui.comboBox_5.addItem("Hardwood")
        self.ui.comboBox_5.addItem("Oil Palm Fiber")

        # wall materials
        self.ui.comboBox_4.addItem("Dense Cast Concrete")
        self.ui.comboBox_4.addItem("Light Cast Concrete")
        self.ui.comboBox_4.addItem("Compacted Earth Brick")
        self.ui.comboBox_4.addItem("Reeds")
        self.ui.comboBox_4.addItem("Bagasse")
        self.ui.comboBox_4.addItem("Cotton Stalks")
        self.ui.comboBox_4.addItem("Date Palm")
        self.ui.comboBox_4.addItem("Pineapple Leaves")
        self.ui.comboBox_4.addItem("Oil Palm Fiber")
        self.ui.comboBox_4.addItem("Straw Bale")

        # roof materials
        self.ui.comboBox_6.addItem("Dense Cast Concrete")
        self.ui.comboBox_6.addItem("Light Cast Concrete")
        self.ui.comboBox_6.addItem("Straw")
        self.ui.comboBox_6.addItem("Bamboo")
        self.ui.comboBox_6.addItem("Reeds")
        self.ui.comboBox_6.addItem("Bagasse")
        self.ui.comboBox_6.addItem("Cotton Stalks")
        self.ui.comboBox_6.addItem("Date Palm")
        self.ui.comboBox_6.addItem("Pineapple Leaves")
        self.ui.comboBox_6.addItem("Oil Palm Fiber")

        # IS THIS REDUNDANT? connect the calculate button to the calculation function
        self.ui.commandLinkButton.clicked.connect(self.calculate_ewb_score)

    def calculate_ewb_score(self):
        # get values from UI
        floor_area = float(self.ui.lineEdit.text())
        wall_area = float(self.ui.lineEdit_2.text())
        window_area = float(self.ui.lineEdit_3.text())
        roof_area = float(self.ui.lineEdit_4.text())

        #calculate the baseline
        baseline_Ri = [4, 2.86, 3.33] # thermal resistance of floor, wall, roof
        Afloor = floor_area
        Awall = wall_area
        Aroof = roof_area

        baseline_u_value = 1/(sum(baseline_Ri) + (Afloor/0.25) + (Awall/0.35) + (Aroof/0.30))

        # matrials from dropdown menus
        Floor_material = self.ui.comboBox_5.currentText()
        Wall_material = self.ui.comboBox_4.currentText()
        Roof_material = self.ui.comboBox_6.currentText()

        # get thickness from linEdits
        floor_thickness = float(self.ui.lineEdit_9.text())
        wall_thickness = float(self.ui.lineEdit_10.text())
        window_thickness = float(self.ui.lineEdit_11.text())
        roof_thickness = float(self.ui.lineEdit_12.text())

        # get R-values
        if Floor_material == 'Dense Cast Concrete':
            R_value_floor = (floor_thickness/1000) / dense_cast_concrete
        elif Floor_material == 'Light Cast Concrete':
            R_value_floor = (floor_thickness/1000) / light_cast_concrete
        elif Floor_material == 'Oil Palm Fiber':
            R_value_floor = (floor_thickness/1000) / oil_palm_fiber
        else:
            R_value_floor = (floor_thickness/1000) / hardwood

        if Wall_material == 'Dense Cast Concrete':
            R_value_wall = (wall_thickness/1000) / dense_cast_concrete
        elif Wall_material == 'Light Cast Concrete':
            R_value_wall = (wall_thickness/1000) / light_cast_concrete
        elif Wall_material == 'Reeds':
            R_value_wall = (wall_thickness/1000) / reeds
        elif Wall_material == 'Bagasse':
            R_value_wall = (wall_thickness/1000) / bagasse
        elif Wall_material == 'Cotton Stalks':
            R_value_wall = (wall_thickness/1000) / cotton_stalks
        elif Wall_material == 'Date Palm':
            R_value_wall = (wall_thickness/1000) / date_palm
        elif Wall_material == 'Pineapple Leaves':
            R_value_wall = (wall_thickness/1000) / pineapple_leaves
        elif Wall_material == 'Oil Palm Fiber':
            R_value_wall = (wall_thickness/1000) / oil_palm_fiber
        elif Wall_material == 'Straw Bale':
            R_value_wall = (wall_thickness/1000) / straw_bale
        else:
            R_value_wall = (wall_thickness/1000) / compacted_earth_brick

        R_value_window = (window_thickness/1000) / glass

        if Roof_material == 'Dense Cast Concrete':
            R_value_roof = (roof_thickness/1000) / dense_cast_concrete
        elif Roof_material == 'Light Cast Concrete':
            R_value_roof = (roof_thickness/1000) / light_cast_concrete
        elif Roof_material == 'Straw':
            R_value_roof = (roof_thickness/1000) / straw
        elif Roof_material == 'Reeds':
            R_value_roof = (roof_thickness/1000) / reeds
        elif Roof_material == 'Bagasse':
            R_value_roof = (roof_thickness/1000) / bagasse
        elif Roof_material == 'Cotton Stalks':
            R_value_roof = (roof_thickness/1000) / cotton_stalks
        elif Roof_material == 'Date Palm':
            R_value_roof = (roof_thickness/1000) / date_palm
        elif Roof_material == 'Pineapple Leaves':
            R_value_roof = (roof_thickness/1000) / pineapple_leaves
        elif Roof_material == 'Oil Palm Fiber':
            R_value_roof = (roof_thickness/1000) / oil_palm_fiber
        else:
            R_value_roof = (roof_thickness/1000) / bamboo

        #calculate design u-value
        Ri = [R_value_floor, R_value_wall, R_value_roof]
        Afloor = floor_area
        Ufloor = 1/R_value_floor
        Awall = wall_area
        Uwall = 1/R_value_wall
        Awin = window_area
        Uwin = 1/R_value_window
        Aroof = roof_area
        Uroof = 1/R_value_roof

    
        calculate_design_u_value = 1/(sum(Ri) + (Awin/Uwin) + (Awall/Uwall) + (Afloor/Ufloor) + (Aroof/Uroof))
        if calculate_design_u_value <= baseline_u_value:
            result = f"Your design has an overall U-value of {calculate_design_u_value:.5f} W/m².K, is equal to or less than \nthe baseline of {baseline_u_value:.5f} W/m².K for a building \nthis size and is therefore an appropriate design."
        else:
            result = f"Your design has an overall U-value of {calculate_design_u_value:.5f} W/m².K, greater than \nthe baseline of {baseline_u_value:.5f} W/m².K for a building this size and therefore \nmay need further components to reduce the U-value."
        
        #controlling the command link button "calculate now"
        self.ui.commandLinkButton.clicked.connect(self.calculate_ewb_score)

        #attempting to make lblCalculation result display message
        self.ui.lblCalculationResult.setText(str(result))


if __name__ == '__main__':
    app = qtw.QApplication([])
    calc = EWBCalculator()
    calc.show()
    app.exec()