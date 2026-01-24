"""
Examples of basic string slicing using a phone number.
Demonstrates:
- slicing from the start
- slicing from the end
- slicing with explicit ranges
"""

phone = "513-353-8941"

# Area code
print(phone[0:3])

# Last four digits (explicit range)
print(phone[8:12])

# Last four digits (slice to end)
print(phone[8:])

