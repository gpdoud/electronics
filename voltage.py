# Voltage calculations

def calc_voltage(I, R):
    """Calculates voltage given current (I) and resistance (R)"""
    return I * R

def calc_current_from_voltage(V, R):
    """Calculates current given voltage (V) and resistance (R)"""
    return V / R

def calc_resistance_from_voltage(V, I):
    """Calculates resistance given voltage{V} and current (I)"""
    return V / I