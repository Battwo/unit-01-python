

print()
print()
inspector=  input("Enter inspector ID: ") # we ask for your id


batch_id = input("Enter batch ID: ") # we asked for the id 
batch_size = int(input("Enter batch size: ")) # the size of the batch 

total_quality_score = 0
my_dict = { #I made a Dictionary


  "none": 0,
  "minor": 0,
  "major": 0
}
 

for x in range(batch_size): # based on the total of the batch size thw question will repeat as mant times as the batch size is 
     print(x)

     score = float(input("whats the quality score?:")) # after getting the score of all the items it will add it up and devide it by the batch size 
     total_quality_score += score


print(total_quality_score/batch_size) 