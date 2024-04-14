from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QGroupBox, QHBoxLayout, QVBoxLayout,
    QSpinBox, QDoubleSpinBox, QLabel, QComboBox)

from converters.data_converter import DataConverter
from converters.length_converter import LengthConverter
from converters.temperature_converter import TemperatureConveter
from converters.weight_conveter import WeightConverter

class AppWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Universal converter')
        self.setMinimumWidth(320)

        # region Initialize instances
        self.from_temperature_input =  QDoubleSpinBox()
        self.from_temperature_unit = QComboBox()
        self.to_temperature_label = QLabel('0')
        self.to_temperature_unit = QComboBox()

        self.from_weight_input = QDoubleSpinBox()
        self.from_weight_unit = QComboBox()
        self.to_weight_label = QLabel('0')
        self.to_weight_unit = QComboBox()

        self.from_length_input = QDoubleSpinBox()
        self.from_length_unit = QComboBox()
        self.to_length_label = QLabel('0')
        self.to_length_unit = QComboBox()

        self.from_data_input = QSpinBox()
        self.from_data_unit = QComboBox()
        self.to_data_label = QLabel('0')
        self.to_data_unit = QComboBox()
        
        self.temperature_converter = TemperatureConveter()
        self.weight_converter = WeightConverter()
        self.length_converter = LengthConverter()
        self.data_converter = DataConverter()
        # endregion
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.init_and_get_temperature_group())
        main_layout.addWidget(self.init_and_get_weight_group())
        main_layout.addWidget(self.init_and_get_length_group())
        main_layout.addWidget(self.init_and_get_data_group())

        self.setLayout(main_layout)

    # region Temperature
    def init_and_get_temperature_group(self) -> QGroupBox:
        temperature_group = QGroupBox('Temperature')
        temperature_layout = QHBoxLayout()

        self.from_temperature_input.setValue(0)
        self.from_temperature_input.setRange(-99999, 99999)
        self.from_temperature_input.valueChanged.connect(self.from_temperature_changed)

        self.from_temperature_unit.addItems(self.temperature_converter.conversion_rates.keys())
        self.to_temperature_unit.addItems(self.temperature_converter.conversion_rates.keys())
        self.from_temperature_unit.currentIndexChanged.connect(self.temperature_unit_changed)
        self.to_temperature_unit.currentIndexChanged.connect(self.temperature_unit_changed)

        temperature_layout.addWidget(self.from_temperature_input)
        temperature_layout.addWidget(self.from_temperature_unit)
        self.add_is_label_to_layout(temperature_layout)
        temperature_layout.addWidget(self.to_temperature_label)
        temperature_layout.addWidget(self.to_temperature_unit)

        temperature_group.setLayout(temperature_layout)

        return temperature_group
    
    def from_temperature_changed(self, value):
        from_unit = self.from_temperature_unit.currentText()
        to_unit = self.to_temperature_unit.currentText()
        result = self.temperature_converter.convert(value, from_unit, to_unit)
        self.to_temperature_label.setText('{:.3f}'.format(result))

    def temperature_unit_changed(self, combo_box_index):
        from_unit = self.from_temperature_unit.currentText()
        to_unit = self.to_temperature_unit.currentText()
        value = self.from_temperature_input.value()
        result = self.temperature_converter.convert(value, from_unit, to_unit)
        self.to_temperature_label.setText('{:.3f}'.format(result))
    #endregion

    # region Weight & Mass
    def init_and_get_weight_group(self) -> QGroupBox:
        weight_group = QGroupBox('Weight and Mass')
        weight_layout = QHBoxLayout()

        self.from_weight_input.setValue(0)
        self.from_weight_input.setRange(-99999, 99999)
        self.from_weight_input.valueChanged.connect(self.from_weight_changed)

        self.from_weight_unit.addItems(self.weight_converter.conversion_rates.keys())
        self.to_weight_unit.addItems(self.weight_converter.conversion_rates.keys())
        self.from_weight_unit.currentIndexChanged.connect(self.weight_unit_changed)
        self.to_weight_unit.currentIndexChanged.connect(self.weight_unit_changed)
        
        weight_layout.addWidget(self.from_weight_input)
        weight_layout.addWidget(self.from_weight_unit)
        self.add_is_label_to_layout(weight_layout)
        weight_layout.addWidget(self.to_weight_label)
        weight_layout.addWidget(self.to_weight_unit)

        weight_group.setLayout(weight_layout)

        return weight_group
    
    def from_weight_changed(self, value):
        from_unit = self.from_weight_unit.currentText()
        to_unit = self.to_weight_unit.currentText()
        result = self.weight_converter.convert(value, from_unit, to_unit)
        self.to_weight_label.setText('{:.3f}'.format(result))

    def weight_unit_changed(self, combo_box_index):
        from_unit = self.from_weight_unit.currentText()
        to_unit = self.to_weight_unit.currentText()
        value = self.from_weight_input.value()
        result = self.weight_converter.convert(value, from_unit, to_unit)
        self.to_weight_label.setText('{:.3f}'.format(result))
    #endregion

    # region Length
    def init_and_get_length_group(self) -> QGroupBox:
        length_group = QGroupBox('Length')
        length_layout = QHBoxLayout()

        self.from_length_input.setValue(0)
        self.from_length_input.setRange(-99999, 99999)
        self.from_length_input.valueChanged.connect(self.from_length_changed)

        self.from_length_unit.addItems(self.length_converter.conversion_rates.keys())
        self.to_length_unit.addItems(self.length_converter.conversion_rates.keys())
        self.from_length_unit.currentIndexChanged.connect(self.length_unit_changed)
        self.to_length_unit.currentIndexChanged.connect(self.length_unit_changed)

        length_layout.addWidget(self.from_length_input)
        length_layout.addWidget(self.from_length_unit)
        self.add_is_label_to_layout(length_layout)
        length_layout.addWidget(self.to_length_label)
        length_layout.addWidget(self.to_length_unit)

        length_group.setLayout(length_layout)

        return length_group
    
    def from_length_changed(self, value):
        from_unit = self.from_length_unit.currentText()
        to_unit = self.to_length_unit.currentText()
        result = self.length_converter.convert(value, from_unit, to_unit)
        self.to_length_label.setText('{:.3f}'.format(result))

    def length_unit_changed(self, combo_box_index):
        from_unit = self.from_length_unit.currentText()
        to_unit = self.to_length_unit.currentText()
        value = self.from_length_input.value()
        result = self.length_converter.convert(value, from_unit, to_unit)
        self.to_length_label.setText('{:.3f}'.format(result))
    #endregion

    # region Data
    def init_and_get_data_group(self) -> QGroupBox:
        data_group = QGroupBox('Data')
        data_layout = QHBoxLayout()

        self.from_data_input.setValue(0)
        self.from_data_input.setRange(0, 10**7)
        self.from_data_input.valueChanged.connect(self.from_data_changed)

        self.from_data_unit.addItems(self.data_converter.conversion_rates.keys())
        self.to_data_unit.addItems(self.data_converter.conversion_rates.keys())
        self.from_data_unit.currentIndexChanged.connect(self.data_unit_changed)
        self.to_data_unit.currentIndexChanged.connect(self.data_unit_changed)

        data_layout.addWidget(self.from_data_input)
        data_layout.addWidget(self.from_data_unit)
        self.add_is_label_to_layout(data_layout)
        data_layout.addWidget(self.to_data_label)
        data_layout.addWidget(self.to_data_unit)

        data_group.setLayout(data_layout)

        return data_group
    
    def from_data_changed(self, value):
        from_unit = self.from_data_unit.currentText()
        to_unit = self.to_data_unit.currentText()
        result = self.data_converter.convert(value, from_unit, to_unit)
        self.to_data_label.setText('{:.3f}'.format(result))

    def data_unit_changed(self, combo_box_index):
        from_unit = self.from_data_unit.currentText()
        to_unit = self.to_data_unit.currentText()
        value = self.from_data_input.value()
        result = self.data_converter.convert(value, from_unit, to_unit)
        self.to_data_label.setText('{:.3f}'.format(result))
    #endregion

    def add_is_label_to_layout(self, layout: QHBoxLayout):
        is_label = QLabel('is')
        layout.addWidget(is_label, alignment = Qt.AlignmentFlag.AlignCenter)