# list = [63,652,611,60]
list=["abc","av","agdsd","ad"]
print("Given list : ",list)
if all(str(i)[0] == str(list[0])[0] for i in list):
   print("True")
else:
   print("False")
   


# my_tuple = ('sara', 6, 5, 0.97)
# my_list = ['sara', 6, 5, 0.97]
# print(my_tuple[0]) # output => 'sara'
# print(my_list[0]) # output => 'sara'
# # my_tuple[0] = 'ansh' # modifying tuple => throws an error
# my_list[0] = 'ansh' # modifying list => list modified
# print(my_tuple[0]) # output => 'sara'
# print(my_list[0]) # output => 'ansh'
