def main():
    time_input = input("What time is it? ")
    time = convert(time_input)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print("not meal time")


def convert(time):
    # Normalize input
    time = time.strip().lower()
    time = time.replace(".", "").replace(" ", "")

    # Handle 12-hour format
    if "am" in time or "pm" in time:
        if "am" in time:
            period = "am"
            time_part = time.replace("am", "")
        else:
            period = "pm"
            time_part = time.replace("pm", "")

        if ":" not in time_part:
            raise ValueError("Invalid time format. Expected HH:MM.")

        hours, minutes = time_part.split(":")
        hours = float(hours)
        minutes = float(minutes)

        if period == "pm" and hours != 12:
            hours += 12
        if period == "am" and hours == 12:
            hours = 0

    else:
        # 24-hour format
        if ":" not in time:
            raise ValueError("Invalid time format. Expected HH:MM.")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)

    return hours + minutes / 60


if __name__ == "__main__":
    main()



