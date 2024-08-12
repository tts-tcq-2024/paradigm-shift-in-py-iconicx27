def is_in_range(value, min_val, max_val):
    return min_val <= value <= max_val

def print_warning(value, min_val, max_val, parameter_name):
    warning_margin = (max_val - min_val) * 0.05
    if value <= min_val + warning_margin:
        print(f"Warning: {parameter_name} approaching lower limit!")
    elif value >= max_val - warning_margin:
        print(f"Warning: {parameter_name} approaching upper limit!")

def check_parameter(value, min_val, max_val, parameter_name):
    if not is_in_range(value, min_val, max_val):
        print(f"{parameter_name} is out of range!")
        return False
    print_warning(value, min_val, max_val, parameter_name)
    return True

def check_charge_rate(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    elif charge_rate > 0.8 * 0.95:
        print('Warning: Charge rate approaching upper limit!')
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (check_parameter(temperature, 0, 45, 'Temperature') and
            check_parameter(soc, 20, 80, 'State of Charge') and
            check_charge_rate(charge_rate))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
    assert(battery_is_ok(42, 78, 0.78) is True) #warning condition
    assert(battery_is_ok(10, 22, 0.79) is True) #warning condition
