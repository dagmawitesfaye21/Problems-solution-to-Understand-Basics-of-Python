tuition = 10000
yearly_increase_percentage = 0.05
tuition_in_ten_years = 0
four_years_of_tuition = 0
year = 0
while(year<11):
    tuition = tuition * 1.05
    if(year == 10):
        yearly_increase_percentage = tuition
    year += 1
    
print("Tuition in ten years: ", round(yearly_increase_percentage, 2))

for year in range(10,14,1):
    yearly_increase_percentage = yearly_increase_percentage * 1.05
    four_years_of_tuition = yearly_increase_percentage + four_years_of_tuition
    
print("The four year total tuition in ten years is: ",round(four_years_of_tuition, 2))