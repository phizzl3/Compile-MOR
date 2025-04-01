def _add_loop() -> int:
    """
    Continuously prompts the user to add numeric values until '0' is entered.
    Returns the sum of all entered values.
    """
    total = []

    print(' Enter "0" when done...')
    while not total or total[-1]:
        user_input = input(" Add: ")
        if not user_input.isnumeric():
            print(" Try again...")
            continue
        total.append(int(user_input))

    return sum(total)


def _will_it_float(entry: str) -> bool:
    """
    Checks if the entry can be converted to a float.
    If not, prints an error message and returns False.
    """
    try:
        float(entry)
    except ValueError:
        print(" Invalid format.  Try again...")
        return False
    return True


def _calculate_postage(data: dict) -> None:
    """
    Prompts the user to enter the beginning meter balance, postage added,
    and ending meter balance. Calculates the cost of outbound mail and
    updates the data dictionary.
    """
    meter_start = 0
    meter_end = 0

    print("\n *Postage Usage*")

    float_verification = False
    while not float_verification:
        meter_start = input("\n Enter the BEGINNING METER BALANCE: ")
        float_verification = _will_it_float(meter_start)
        meter_start = float(meter_start)

    print(" Enter each POSTAGE ADDED amount.")
    postage_added = _add_loop()

    float_verification = False
    while not float_verification:
        meter_end = input(" Enter the ENDING METER BALANCE for the Month: ")
        float_verification = _will_it_float(meter_end)
        meter_end = float(meter_end)

    data["Postage Spend"] = meter_start + postage_added - meter_end


def _get_mail_volumes_input(data: dict):
    """
    Prompts the user to enter daily totals for various mail types.
    Updates the data dictionary with the total volumes.
    """
    print("\n *Mail Volumes*")
    for mail_type in (
        "Outbound Mail",
        "Inbound Mail",
        "Returned Mail",
        "Outbound Accountable Mail",
        "Inbound Accountable Mail",
    ):
        print(f"\n Enter each day's total from the {mail_type} column.")
        data[mail_type] = 0
        data[mail_type] = _add_loop()


def calculate_mail_totals(data: dict) -> None:
    """
    Calculates and updates the total volumes for mail usage.
    """
    _calculate_postage(data)
    _get_mail_volumes_input(data)
