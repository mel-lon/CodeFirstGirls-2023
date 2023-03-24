# Here is a snippet of Lionel Richie’s song “All Night Long (All Night)”

        # Well, my friends, the time has come
        # To raise the roof and have some fun
        # Throw away the work to be done
        # Let the music play on (play on, play on, play on...)
        # Everybody sing, everybody dance
        # Lose yourself in wild romance
        # We're going to Party, Karamu, Fiesta, forever
        # Come on and sing along!
        #
        # All night long (all night), All night (all night)
        # All night long (all night), All night (all night)
        # All night long (all night), All night (all night)
        # All night long! (all night), Ooh, yeah (all night)
        #
        # People dancing all in the street
        # See the rhythm all in their feet
        # Life is good, wild and sweet
        # Let the music play on...(Play on, play on, play on...)
        # Feel it in your heart and feel it in your soul
        # Let the music take control
        # We're going to Party, Liming, Fiesta, forever
        # Come on and sing along
        # We're going to Party, Liming, Fiesta, forever
        # Come on and sing my song!
        #
# Tasks:
# 1.	Write the lyrics to a new file called song.txt

file= open('song.txt','w')
file.write("Well, my friends, the time has come\n"
           "To raise the roof and have some fun\n"
           "Throw away the work to be done\n"
           "Let the music play on (play on, play on, play on...)\n"
           "Everybody sing,\n everybody dance\n"
           "Lose yourself in wild romance\n"
           "We're going to Party, Karamu, Fiesta, forever\n"
           "Come on and sing along!\n"
           "All night long (all night),\n All night (all night)\n"
           "All night long (all night),\n All night (all night)\n"
           "All night long (all night),\n All night (all night)\n"
           "All night long! (all night),\n Ooh, yeah (all night)\n"
           "People dancing all in the street\n"
           "See the rhythm all in their feet\n"
           "Life is good, wild and sweet\n"
           "Let the music play on...(Play on, play on, play on...)\n"
           "Feel it in your heart and feel it in your soul\n"
           "Let the music take control\n"
           "We're going to Party, Liming, Fiesta, forever\n"
           "Come on and sing along\n"
           "We're going to Party, Liming, Fiesta, forever\n"
           "Come on and sing my song!\n")


file.close()
# 2.	Read in the file and print out ONLY lines that have the word ‘sing’ in them.

filtered = []
with open("song.txt", "r") as file:
    for line in file:
        if 'sing' in line:
            print(line)



