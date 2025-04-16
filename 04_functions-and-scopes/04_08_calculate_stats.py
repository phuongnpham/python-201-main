# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(num_list):
  """Find the maximum, minimum, average and sum of the numbers

  Args:
      num_list (list): A list of numbers
  """
  max_number = max(num_list)
  min_number = min(num_list)
  sum_number = sum(num_list)
  avg_number = sum_number / len(num_list)

  print(f"Maximum number: {max_number}")
  print(f"Minimum number: {min_number}")
  print(f"Sum of the numbers: {sum_number}")
  print(f"Average of the numbers: {avg_number}")

# call the function below here
stats(example_list)
