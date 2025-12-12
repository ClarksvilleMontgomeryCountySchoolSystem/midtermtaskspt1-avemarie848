# TEST DATA - Do not modify
creator_name = "DigitalDreamer"
current_followers = 4567
starting_followers = 2100
days_tracked = 45
milestone_increment = 1000

# YOUR CODE BELOW THIS LINE
# Calculate follower statistics and milestone progress

# Calculate milestone progress
current_milestone = current_followers // milestone_increment
progress_in_milestone = current_followers % milestone_increment

# Calculate growth statistics
total_gained = current_followers - starting_followers
daily_average = total_gained // days_tracked

# Calculate projections
days_to_milestone = (milestone_increment - progress_in_milestone) // daily_average
weekly_growth = daily_average * 7

# Display results with f-strings
print(f"Creator: {creator_name}")
print(f"Curent milestone: {current_milestone}")
print(f"Progress in milestone: {progress_in_milestone}")
print(f"Total Growth: {total_gained} followers")
print(f"Daily average: {daily_average} followers")
print(f"Days to next milestone: {days_to_milestone} days")
print(f"Weekly growth projection: {weekly_growth} followers")
