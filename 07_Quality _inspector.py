

print()
print()
inspector=  input("Enter inspector ID: ")


batch_id = input("Enter batch ID: ")
batch_size = int(input("Enter batch size: "))

total_quality_score = 0
my_dict = { #I made a Dictionary


  "none": 0,
  "minor": 0,
  "major": 0
}
 

for x in range(batch_size):
     print(x)

     score = float(input("whats the quality score?:"))
     total_quality_score += score


print(total_quality_score/batch_size)