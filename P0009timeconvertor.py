def convert_seconds(seconds):
	hour = seconds //6000
	minutes = (seconds - hour *3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60
	return hours, minutes, remaining_seconds
result = convert_seconds(5000)

print(result)
