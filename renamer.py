from pathlib import Path

def preview(folder):
   count = 1
   for f in sorted(folder.iterdir()):
    if f.is_file():
        new_name =f"photo_{count:03d}{f.suffix}"
        print(f.name, "->", new_name)
        count +=1


def rename_files(folder):
   count = 1
   for f in sorted(folder.iterdir()):
     
       if f.is_file():
          new_name =f"photo_{count:03d}{f.suffix}"
          target = f.with_name(new_name)
          if target == f:
              pass
          elif target.exists(): 
           print("Skipped, already exists:", new_name)
          else:
           f.rename(target)
          count +=1
    
Folder_name = input("Enter the folder name: ")
folder = Path(Folder_name) 

try:
   preview(folder)
   answer = input("Rename these files?(y/n): ")
   if answer == "y":
      rename_files(folder)
      print("Done")
   else:
      print("Cancelled.")  
except FileNotFoundError:
   print("Folder not found, check the name.")      
    
