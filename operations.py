def basic_operation(operand1, operand2, operator):
  if operator == "+":
    return operand1 + operand2
  elif operator == "-":
    return operand1 - operand2
  elif operator == "*":
    return operand1 * operand2
  elif operator == "/":
    if operand2 != 0:
      return operand1 / operand2
    else:
      raise ValueError("Cannot divide by zero")
  else:
    raise ValueError("Invalid operator")