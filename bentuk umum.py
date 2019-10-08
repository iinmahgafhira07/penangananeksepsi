def main():
  try:
  
    f = open("data.txt", "r"
    
    try:
    
        f.write("pemrongraman python")
    finally:
       f.close()
  except IOError:
    print("\nERROR: File tidak dapat " + "dibuka/ditulis")
    
if __name__ == "__main__":
    main()
