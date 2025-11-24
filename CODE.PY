import datetime as dt
from datetime import date, timedelta
import sys 

def convert_to_date(value_str):
  try:
    # Expecting dd-mm-yyyy and returning a date object
    return dt.datetime.strptime(value_str, "%d-%m-%Y").date()
  except ValueError:
    print("Invalid date format. Please input a valid date (dd-mm-yyyy).")
    sys.exit()

def convert_to_int(value_str):
    try:
        return int(value_str)
    except ValueError:
        print("Invalid input. Please enter a number.")
        sys.exit()

def calculate_ovulation_date(previous_period_start_date, avg_cycle_length):

  estimate_ovulation_day_offset = avg_cycle_length - 14
  ovulation_day_delta = timedelta(days=estimate_ovulation_day_offset)
  ovulation_date = previous_period_start_date + ovulation_day_delta
  return ovulation_date

def track_cycle():
  print("\n--- Menstrual Cycle Tracker ---")
  
  previous_period_start_input = input("Please enter the date at which your last period started? (dd-mm-yyyy): ")
  previous_period_start = convert_to_date(previous_period_start_input)
  
  period_duration_input = input("Please enter the duration of your average period (in days): ")
  period_duration = convert_to_int(period_duration_input)
  
  avg_cycle_length_input = input("Please enter the average number of days between your periods: ")
  avg_cycle_length = convert_to_int(avg_cycle_length_input)
  
  ovulation_date = calculate_ovulation_date(previous_period_start, avg_cycle_length)
  print(f"Estimated ovulation date: {ovulation_date.strftime('%Y-%m-%d')}")

def main():
    track_cycle()
if_ name_ == "_main_"
    