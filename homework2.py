number_of_completed_remote_sensing = 12
number_of_hours_spent = 1.5
course_name = 'Python'
time_per_task = number_of_hours_spent / number_of_completed_remote_sensing

# Решенеие 1
print("Курс: " + str(course_name)+ ", "+
      "всего задач: " + str(number_of_completed_remote_sensing) + ", " +
      "затрачено часов: " + str(number_of_hours_spent) + ", " +
      "среднее время выполнения " + str(time_per_task) + " часа.")

# Решение 2, но не знаю как поставить запятые после присвоения переменной, могу так же как выше (решение 1) добавить запятые, может есть еще какой-нибудь другой способ?
print("Курс:", course_name, "всего задач:" ,
      number_of_completed_remote_sensing,"затрачено часов: " ,
      number_of_hours_spent, "среднее время выполнения " ,
      time_per_task, "часа.")

# решение 3, изучил самостоятельно
print(f"Курс: {course_name}, "                                               
      f"всего задач: {number_of_completed_remote_sensing}, "
      f"затрачено часов: {number_of_hours_spent}, "
      f"среднее время выполнения {time_per_task} часа.")