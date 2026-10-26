def check_premium(answer):
    if (answer.strip().lower().startswith('y')):
        return True
    elif (answer.strip().lower().startswith('n')):
        return False

def exceeds_data_limit(data_used):
    if (data_used > 10):
        return True
    else:
        return False

def get_overage_rate(data_used, has_premium):
    if (data_used <= 10):
        return 0
    elif (data_used <= 20 and has_premium):
        return 1
    elif ((data_used <= 20 and not has_premium) or (data_used > 20 and has_premium)):
        return 2
    else:
        return 3


def main():
    GB = float(input("Enter data used (GB): "))
    baseCost = round(float(input("Enter base monthly plan cost: ")), 2)
    premium = check_premium(input("Do you have a premium plan? (yes or no): "))
    over = exceeds_data_limit(GB)
    overageRate = get_overage_rate(GB, premium)
    bill = baseCost
    if (exceeds_data_limit(GB)):
        overAmnt = GB-10
        extraCharge = round(overAmnt*overageRate, 2)
        bill += extraCharge
        print(f"\nYou are {overAmnt} GB over your limit")
        print(f"Overage Rate: ${overageRate} per GB")
    else:
        extraCharge = 0
        print("\nYou are within your data limit.\nGB over limit: 0")
    print(f"Overage Cost: ${extraCharge:.2f}")
    print(f"Total bill: ${bill:.2f}")


# Keep this guard: importing functions for tests must not prompt for input.
if __name__ == "__main__":
    main()
