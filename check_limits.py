def check_in_range(value, min_val, max_val, error_message):
    if not (min_val <= value <= max_val):
        print(error_message)
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (check_in_range(temperature, 0, 45, 'Temperature is out of range!') and
            check_in_range(soc, 20, 80, 'State of Charge is out of range!') and
            check_in_range(charge_rate, 0, 0.8, 'Charge rate is out of range!'))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
