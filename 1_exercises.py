#Exercises with lists!

#HELP STORM CATCH THE FISH

#Storm is at position 0. Make her catach the fish and then bring her back to position 0

pool = ["." for _ in range(20)]
storm_pos = 0
fish_pos = 18
storm = "Storm!"
pool[0] = storm

fish_caught = False
while storm_pos <= len(pool):
    print(pool)
    if storm_pos <= fish_pos and not fish_caught:
        pool[storm_pos], pool[storm_pos+1] = ".", storm
        storm_pos+=1
        if storm_pos == fish_pos:
            print("YUMMY YUMMY YUMMY! Gimme gimme gimme")
            fish_caught = True
            print(storm_pos)
    else:
        pool[storm_pos], pool[storm_pos-1] = ".", storm
        storm_pos -= 1
        if storm_pos == 0:
            break


