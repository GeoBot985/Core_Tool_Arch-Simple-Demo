# business_methods.py

def open_store(tools):
    tools.unlock_store()
    tools.turn_on_lights()
    tools.notify_staff_store_open()

def process_delivery(tools):
    tools.receive_truck()
    tools.scan_inventory()
    tools.flag_damaged_items()

def close_store(tools):
    tools.count_cash_drawer()
    tools.lock_store()
    tools.notify_security_closing()
