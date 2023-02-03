eventTimeInSeconds = int(input())

hours = 0
minutes = eventTimeInSeconds // 60
seconds = eventTimeInSeconds % 60

if minutes >= 60:
  hours = minutes // 60
  minutes = minutes % 60

print("{0}:{1}:{2}".format(hours, minutes, seconds))