def check_in_range(value, min_val, max_val, warning_min, warning_max, parameter_name):
    if not (min_val <= value <= max_val):
        print(f"{parameter_name} is out of range!")
        return False
    elif value <= warning_min:
        print(f"Warning: {parameter_name} approaching lower limit!")
    elif value >= warning_max:
        print(f"Warning: {parameter_name} approaching upper limit!")
    return True

def is_charge_rate_ok(charge_rate, warning_limit=0.76):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    elif charge_rate > warning_limit:
        print('Warning: Charge rate approaching upper limit!')
    return True

def battery_is_ok(temperature, soc, charge_rate):
    temp_warning_margin = 45 * 0.05
    soc_warning_margin = 80 * 0.05
    
    return (check_in_range(temperature, 0, 45, 0 + temp_warning_margin, 45 - temp_warning_margin, 'Temperature') and
            check_in_range(soc, 20, 80, 20 + soc_warning_margin, 80 - soc_warning_margin, 'State of Charge') and
            is_charge_rate_ok(charge_rate))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
