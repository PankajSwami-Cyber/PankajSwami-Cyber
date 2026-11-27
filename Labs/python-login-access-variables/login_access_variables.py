"""Beginner practice: Python variables for a login-access scenario.

Learning exercise only. This does not authenticate users or enforce lockouts.
"""

# Task 1: Store the device identifier as a string.
device_id = "72e08x0"
print("Device ID:", device_id)

# Task 2: Inspect the data type of the device identifier.
device_id_type = type(device_id)
print("Device ID type:", device_id_type)

# Task 3: Store the approved usernames in a list.
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
print("Approved usernames:", username_list)

# Task 5: Reassign the list to include the newly approved username.
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards", "lpope"]
print("Updated approved usernames:", username_list)

# Task 6: Store the maximum permitted login attempts.
max_logins = 3
max_logins_type = type(max_logins)
print("Maximum login attempts type:", max_logins_type)

# Task 7: Store the current number of login attempts.
login_attempts = 2
login_attempts_type = type(login_attempts)
print("Current login attempts type:", login_attempts_type)

# Task 8: Check whether the attempts are within the configured limit.
print("2 attempts within limit:", login_attempts <= max_logins)

# Task 9: Try a value above the limit.
login_attempts = 4
print("4 attempts within limit:", login_attempts <= max_logins)

# Task 10: Store whether the user is currently logged in.
login_status = False
login_status_type = type(login_status)
print("Login status type:", login_status_type)
